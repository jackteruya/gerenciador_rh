from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, viewsets

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.api.rest import BaseAPIViewSet
from empresas.api.serializers import EmpresasSerializer
from empresas.domain.models import Empresas
from empresas.domain.repository import EmpresasRepository
from empresas.services import EmpresasService


class EmpresasAPIView(BaseAPIViewSet):
    # permission_classes = (IsAuthenticated,)
    service = EmpresasService(EmpresasRepository)
    serializer_class = EmpresasSerializer

    @swagger_auto_schema()
    def retrieve(self, request, pk=None):
        """Busca uma empresa pelo ID"""
        return super(EmpresasAPIView, self).retrieve(request, pk=pk)

    @swagger_auto_schema(responses={200: EmpresasSerializer(many=True)})
    def list(self, request):
        """Lista todas as empresas cadastradas"""
        return super(EmpresasAPIView, self).list(request)

    @swagger_auto_schema(request_body=EmpresasSerializer)
    def create(self, request):
        """Cadastrar nova empresa"""
        return super(EmpresasAPIView, self).create(request)

    @swagger_auto_schema(request_body=EmpresasSerializer)
    def update(self, request, pk=None):
        """Atualização da um empresas com base de um ID"""
        return super(EmpresasAPIView, self).update(request, pk)

    @swagger_auto_schema()
    def destroy(self, request, pk=None):
        """Desativa um empresa cadastrada"""
        return super(EmpresasAPIView, self).destroy(request, pk)
