from drf_yasg.utils import swagger_auto_schema
from core.api.rest import BaseAPIViewSet
from departamentos.api.serializers import DepartamentosSerializer
from departamentos.domain.repository import DepartamentosRepository
from departamentos.services import DepartamentosService


class DepartamentosAPIViewSet(BaseAPIViewSet):
    service = DepartamentosService(DepartamentosRepository)
    serializer_class = DepartamentosSerializer

    @swagger_auto_schema()
    def retrieve(self, request, pk=None):
        """Busca uma departamento pelo ID"""
        return super(DepartamentosAPIViewSet, self).retrieve(request, pk=pk)

    @swagger_auto_schema(responses={200: DepartamentosSerializer(many=True)})
    def list(self, request):
        """Lista todas as departamento cadastradas"""
        return super(DepartamentosAPIViewSet, self).list(request)

    @swagger_auto_schema(request_body=DepartamentosSerializer)
    def create(self, request):
        """Cadastrar nova departamento"""
        return super(DepartamentosAPIViewSet, self).create(request)

    @swagger_auto_schema(request_body=DepartamentosSerializer)
    def update(self, request, pk=None):
        """Atualização da um departamento com base de um ID"""
        return super(DepartamentosAPIViewSet, self).update(request, pk)

    @swagger_auto_schema()
    def destroy(self, request, pk=None):
        """Desativa um departamento cadastrada"""
        return super(DepartamentosAPIViewSet, self).destroy(request, pk)
