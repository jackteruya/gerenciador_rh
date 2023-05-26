from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class BaseAPIViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    service = None
    serializer_class = None

    def retrieve(self, request, pk=None):
        try:
            data = self.service.busca_por_id(int(pk))
            serializer = self.serializer_class(data, many=False)
            return Response(serializer.data)
        except Exception:
            return Response(data={'Not Found'}, status=404)

    def list(self, request):
        data = self.service.listar_todos()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            user = 1 if not request.user.id else request.user.id
            data = self.service.cadastrar(request, user)
            serializer = self.serializer_class(data, many=False)
            return Response(serializer.data)
        except Exception as exc:
            return Response({'msg': f'{exc}'}, status=400)

    def update(self, request, pk=None):
        try:
            data = self.service.atualizar(pk, request)
            serializer = self.serializer_class(data, many=False)
            return Response(serializer.data)
        except Exception as exc:
            return Response({'msg': f'{exc}'}, status=400)

    def destroy(self, request, pk=None):
        self.service.remover(pk)
        data = {'msg': 'Removido com sucesso'}
        return Response(data, status=204)
