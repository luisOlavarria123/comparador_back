from rest_framework.routers import DefaultRouter
from .views import ServicioViewSet,RegionViewSet,ServicioPrestacionViewSet,ReseniaViewSet,login,register
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

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



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)