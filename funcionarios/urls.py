from rest_framework import routers

from funcionarios.api.rest import FuncionariosAPIViewSet

router = routers.DefaultRouter()
router.register(r'funcionarios', FuncionariosAPIViewSet, basename='funcionario')

urlpatterns = router.urls
