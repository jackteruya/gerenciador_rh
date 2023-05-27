from django.db import models

from core.domain.models import BasicModel


class Departamentos(BasicModel):
    centro_custo = models.SmallIntegerField()
    nome = models.CharField(max_length=128)
    codigo_integracao = models.CharField(max_length=128)
    empresa = models.ForeignKey('empresas.Empresas', on_delete=models.PROTECT)

    class Meta:
        db_table = 'departamentos'

    def __str__(self):
        return f'{self.nome}'
