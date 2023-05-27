import random

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from empresas.domain.models import Empresas
from departamentos.domain.models import Departamentos
from departamentos.domain.repository import DepartamentosRepository


class DepartamentoRepositoryTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.repository = DepartamentosRepository(Departamentos)
        self.user = User.objects.create(
            id=10,
            email="user@email.com",
            username="usertest",
        )
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
                "centro_custo": 1,
                "nome": "Financeiro",
                "codigo_integracao": "02.01.01.001",
                "empresa_id": self.empresa.id,
                "criado_por_id": self.user.id,
                "atualizado_por_id": self.user.id,
            },
            {
                "centro_custo": 2,
                "nome": "Financeiro",
                "codigo_integracao": "02.01.01.002",
                "empresa_id": self.empresa.id,
                "criado_por_id": self.user.id,
                "atualizado_por_id": self.user.id,
            }
        ]
        self.departamento_0 = Departamentos.objects.create(**self.departamentos_data[0])

    def test_repository_criar_departamento(self):
        response = self.repository.criar(self.departamentos_data[1])

        self.assertTrue(isinstance(response, Departamentos))
        self.assertTrue(Departamentos.objects.filter(id=response.id).exists())

    def test_repository_buscar_departamento_por_id(self):
        response = self.repository.buscar_por_id(self.departamento_0.id)
        self.assertTrue(isinstance(response, Departamentos))

    def test_repository_buscar_departamento_por_id_inexistente(self):
        id = random.randint(10, 100)
        with self.assertRaises(Exception):
            self.repository.buscar_por_id(id)
