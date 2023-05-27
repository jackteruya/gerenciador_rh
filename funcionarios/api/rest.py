from drf_yasg.utils import swagger_auto_schema
from core.api.rest import BaseAPIViewSet
from funcionarios.api.serializers import FuncionariosSerializer
from funcionarios.domain.repository import FuncionariosRepository
from funcionarios.services import FuncionariosService


class FuncionariosAPIViewSet(BaseAPIViewSet):
    service = FuncionariosService(FuncionariosRepository)
    serializer_class = FuncionariosSerializer

    @swagger_auto_schema()
    def retrieve(self, request, pk=None):
        """Busca uma funcionarios pelo ID"""
        return super(FuncionariosAPIViewSet, self).retrieve(request, pk=pk)

    @swagger_auto_schema(responses={200: FuncionariosSerializer(many=True)})
    def list(self, request):
        """Lista todas as funcionarios cadastradas"""
        return super(FuncionariosAPIViewSet, self).list(request)

    @swagger_auto_schema(request_body=FuncionariosSerializer)
    def create(self, request):
        """Cadastrar nova departamento"""
        return super(FuncionariosAPIViewSet, self).create(request)

    @swagger_auto_schema(request_body=FuncionariosSerializer)
    def update(self, request, pk=None):
        """Atualização da um funcionarios com base de um ID"""
        return super(FuncionariosAPIViewSet, self).update(request, pk)

    @swagger_auto_schema()
    def destroy(self, request, pk=None):
        """Desativa um funcionarios cadastrada"""
        return super(FuncionariosAPIViewSet, self).destroy(request, pk)
