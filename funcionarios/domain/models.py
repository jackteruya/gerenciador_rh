from django.db import models

from core.domain.models import BasicModel


class Funcionarios(BasicModel):
    nome = models.CharField(max_length=128)
    sobrenome = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    telefone = models.CharField(max_length=128)
    data_nascimento = models.DateField()
    data_ingresso = models.DateField()
    data_desligamento = models.CharField(null=True, blank=True)
    cidade = models.CharField(max_length=128)
    departamento = models.ForeignKey('departamentos.Departamentos', on_delete=models.PROTECT)
    empresa = models.ForeignKey('empresas.Empresas', on_delete=models.PROTECT)

    class Meta:
        db_table = 'funcionarios'

    def __str__(self):
        return f'{self.nome_completo}'

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
