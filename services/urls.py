from rest_framework.routers import DefaultRouter
from .views import ServicioViewSet,RegionViewSet,ServicioPrestacionViewSet,ReseniaViewSet,login,register
from django.urls import path, include

router = DefaultRouter()
router.register(r'servicios', ServicioViewSet)
router.register(r'regiones', RegionViewSet, basename='region')
router.register(r'servicio-prestaciones', ServicioPrestacionViewSet, basename='servicio-prestacion')
router.register(r'servicio-resenias', ReseniaViewSet, basename='servicio-review')


urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', register),
    path('login/', login),

]