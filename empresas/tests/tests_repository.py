import random

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from empresas.domain.models import Empresas
from empresas.domain.repository import EmpresasRepository


class EmpresasRepositoryTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.repository = EmpresasRepository(Empresas)
        self.user = User.objects.create(
            id=10,
            email="user@email.com",
            username="usertest",
        )
        self.data_empresas = [
            {
                "id": 1,
                "cnpj": "08.319.486/0001-37",
                "logradouro": "rua 1dfasdf0",
                "cidade": "njnofdsafi",
                "pais": "dfasfonopn",
                "ativo": True,
                "criado_por_id": self.user.id,
                "atualizado_por_id": self.user.id,
            },
            {
                "id": 2,
                "cnpj": "26347997000144",
                "logradouro": "rua 1dfasdf0",
                "cidade": "njnofdsafi",
                "pais": "dfasfonopn",
                "ativo": True,
                "criado_por_id": self.user.id,
                "atualizado_por_id": self.user.id,
            }
        ]
        self.empresa_0 = Empresas.objects.create(**self.data_empresas[0])

    def test_repository_criar_empresa(self):
        response = self.repository.criar(self.data_empresas[1])

        self.assertTrue(isinstance(response, Empresas))
        self.assertTrue(Empresas.objects.filter(id=response.id).exists())

    def test_repository_buscar_empresa_por_id(self):
        response = self.repository.buscar_por_id(self.empresa_0.id)
        self.assertTrue(isinstance(response, Empresas))

    def test_repository_criar_empresa_duplicada(self):
        with self.assertRaises(Exception):
            self.repository.criar(self.data_empresas[0])

    def test_repository_buscar_empresa_por_id_inexistente(self):
        id = random.randint(10, 100)
        with self.assertRaises(Exception):
            self.repository.buscar_por_id(id)
