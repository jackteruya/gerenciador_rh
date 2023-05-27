from rest_framework.request import Request

from empresas.domain.models import Empresas


class BaseService:
    def __init__(self, repository):
        self.repository = repository
        self.model = None

    def cadastrar(self, request: Request):
        data = request.data
        data['criado_por_id'] = request.user.id
        data['atualizado_por_id'] = request.user.id
        return self.repository(self.model).criar(request.data)

    def listar_todos(self):
        return self.repository(self.model).listar()

    def busca_por_id(self, id: int):
        return self.repository(self.model).buscar_por_id(id)

    def atualizar(self, id: int, request: Request):
        data = request.data
        data['criado_por_id'] = request.user.id
        return self.repository(self.model).atualizar(id, data)

    def remover(self, id):
        self.repository(self.model).remover(id)
