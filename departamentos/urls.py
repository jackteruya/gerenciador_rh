from rest_framework import routers

from departamentos.api.rest import DepartamentosAPIViewSet

router = routers.DefaultRouter()
router.register(r'departamentos', DepartamentosAPIViewSet, basename='departamento')

urlpatterns = router.urls
