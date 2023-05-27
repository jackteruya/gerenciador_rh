import random

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from departamentos.domain.models import Departamentos
from departamentos.domain.repository import DepartamentosRepository
from departamentos.services import DepartamentosService
from empresas.domain.models import Empresas


class DepartamentosServicesTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=10,
            email="user@email.com",
            username="usertest",
        )
        self.service = DepartamentosService(DepartamentosRepository)
        empresa = {
            "id": 1,
            "cnpj": "08.319.486/0001-37",
            "logradouro": "rua 1dfasdf0",
            "cidade": "njnofdsafi",
            "pais": "dfasfonopn",
            "ativo": True,
            "criado_por_id": self.user.id,
            "atualizado_por_id": self.user.id,
        }
        self.empresa = Empresas.objects.create(**empresa)

        self.departamentos_data = [
            {
                "id": 1,
                "centro_custo": 1,
                "nome": "Financeiro",
                "codigo_integracao": "02.01.01.001",
                "empresa_id": self.empresa.id,
                "criado_por_id": self.user.id,
                "atualizado_por_id": self.user.id,
            },
            {
                "id": 2,
                "centro_custo": 2,
                "nome": "Fiscal",
                "codigo_integracao": "02.01.01.002",
                "empresa_id": self.empresa.id,
                "criado_por_id": self.user.id,
                "atualizado_por_id": self.user.id,
            }
        ]
        self.departamento_0 = Departamentos.objects.create(**self.departamentos_data[0])
        self.request = Request
        self.request.user = self.user

    def test_service_criar_departamento(self):
        departamento_data = self.departamentos_data[1]
        self.request.data = departamento_data
        response = self.service.cadastrar(self.request)

        self.assertEqual(response.codigo_integracao, departamento_data['codigo_integracao'])
        self.assertTrue(Departamentos.objects.filter(id=response.id).exists())

    def test_service_buscar_departamento_por_id(self):
        response = self.service.busca_por_id(self.departamento_0.id)
        self.assertTrue(isinstance(response, Departamentos))

    def test_service_buscar_departamento_por_id_inexistente(self):
        id = random.randint(10, 100)
        with self.assertRaises(Exception):
            self.service.busca_por_id(id)

    def test_service_atualizar_departamento(self):
        departamento_data = self.departamentos_data[0]
        departamento_data['nome'] = 'Contabilidade'
        self.request.data = departamento_data
        response = self.service.atualizar(departamento_data['id'], self.request)

        self.assertEqual(response.nome, departamento_data['nome'])
        self.assertTrue(Empresas.objects.filter(id=response.id).exists())

    def test_service_remover_departamento(self):
        departamento_data = self.departamentos_data[0]
        response = self.service.remover(departamento_data['id'])

        empresa = self.service.busca_por_id(departamento_data['id'])

        self.assertEqual(response, None)
        self.assertEqual(empresa.ativo, False)
        self.assertTrue(Departamentos.objects.filter(id=departamento_data['id']).exists())
