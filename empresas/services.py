import re

from rest_framework.request import Request

from core.services import BaseService
from empresas.domain.models import Empresas


class EmpresasService(BaseService):
    def __init__(self, repository):
        super(EmpresasService, self).__init__(repository)
        self.model = Empresas

    def cadastrar(self, request: Request):
        request.data['cnpj'] = self.validacao_cnpj(request.data['cnpj'])
        return super(EmpresasService, self).cadastrar(request)

    def atualizar(self, id: int, request: Request):
        request.data['cnpj'] = self.validacao_cnpj(request.data['cnpj'])
        return super(EmpresasService, self).atualizar(id, request)

    def validacao_cnpj(self, cnpj):
        if len(cnpj) == 14:
            if not str(cnpj).isdigit():
                raise Exception("CNPJ Invalido")
            return cnpj
        if len(cnpj) == 18:
            cnpj = re.match('^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$', cnpj)
            if not cnpj:
                raise Exception("CNPJ Invalido")
            return ''.join(filter(lambda i: i if i.isdigit() else None, cnpj.group()))
        raise Exception("CNPJ Invalido")
