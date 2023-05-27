from rest_framework import routers

from empresas.api.rest import EmpresasAPIView

router = routers.DefaultRouter()
router.register(r'empresas', EmpresasAPIView, basename='empresa')

urlpatterns = router.urls
