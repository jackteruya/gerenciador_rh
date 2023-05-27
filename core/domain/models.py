from django.db import models


class BasicModel(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='+')
    data_atualizacao = models.DateTimeField(auto_now=True)
    atualizado_por = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='+')
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True
