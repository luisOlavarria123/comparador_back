from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, login,register
from django.urls import path, include

router = DefaultRouter()
router.register(r'servicios', ServiceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', register),
    path('login/', login),
]