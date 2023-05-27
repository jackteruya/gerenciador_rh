import random

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from empresas.domain.models import Empresas
from empresas.domain.repository import EmpresasRepository
from empresas.services import EmpresasService


class EmpresasServicesTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=10,
            email="user@email.com",
            username="usertest",
        )
        self.service = EmpresasService(EmpresasRepository)
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
        self.request = Request
        self.request.user = self.user
        self.empresa_0 = Empresas.objects.create(**self.data_empresas[0])

    def test_service_criar_empresa(self):
        empresa_data = self.data_empresas[1]
        self.request.data = empresa_data
        response = self.service.cadastrar(self.request)

        self.assertEqual(response.cnpj, empresa_data['cnpj'])
        self.assertTrue(Empresas.objects.filter(id=response.id).exists())

    def test_service_buscar_empresa_por_id(self):
        response = self.service.busca_por_id(self.empresa_0.id)
        self.assertTrue(isinstance(response, Empresas))

    def test_service_criar_empresa_duplicada(self):
        with self.assertRaises(Exception):
            self.service.cadastrar(self.data_empresas[0])

    def test_service_buscar_empresa_por_id_inexistente(self):
        id = random.randint(10, 100)
        with self.assertRaises(Exception):
            self.service.busca_por_id(id)

    def test_service_atualizar_empresa(self):
        empresa_data = self.data_empresas[0]
        empresa_data['logradouro'] = 'Avenida 2023'
        self.request.data = empresa_data
        response = self.service.atualizar(empresa_data['id'], self.request)

        self.assertEqual(response.logradouro, empresa_data['logradouro'])
        self.assertTrue(Empresas.objects.filter(id=response.id).exists())

    def test_service_remover_empresa(self):
        empresa_data = self.data_empresas[0]
        response = self.service.remover(empresa_data['id'])

        empresa = self.service.busca_por_id(empresa_data['id'])

        self.assertEqual(response, None)
        self.assertEqual(empresa.ativo, False)
        self.assertTrue(Empresas.objects.filter(id=empresa_data['id']).exists())
