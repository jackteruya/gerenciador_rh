from typing import Dict

from django.db.models import Q
from rest_framework.exceptions import NotFound


class BaseRepository:
    def buscar_por_id(self, id: int):
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            raise NotFound()

    def buscar_query(self, query):
        return self.model.objects.filter(query)

    def listar(self):
        return self.model.objects.all()

    def criar(self, data: Dict):
        return self.model.objects.create(**data)

    def atualizar(self, id: int, data: Dict, query=Q()):
        self.model.objects.filter(id=id).filter(query).update(**data)
        return self.buscar_por_id(id)

    def remover(self, id: int):
        obj = self.buscar_por_id(id)
        if not obj or not obj.ativo:
            raise NotFound('Not Found')
        obj.ativo = False
        obj.save(update_fields=['ativo', ])
