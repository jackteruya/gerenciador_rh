from django.db import models

from core.domain.models import BasicModel


class Empresas(BasicModel):
    cnpj = models.CharField(max_length=18, unique=True)
    logradouro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    pais = models.CharField(max_length=128)

    class Meta:
        db_table = 'empresas'

    def __str__(self):
        return f'{self.cnpj}'
