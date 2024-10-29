from rest_framework import viewsets
from .models import Servicio, Resenia, Region, ServicioPrestacion
from .serializers import ServicioSerializer, ReseniaSerializer, RegionSerializer,ServicioPrestacionSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ServicioFilter, ServicioPrestacionFilter,ReseniaFilter

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    filter_backends = [DjangoFilterBackend]  # Habilitar el backend de filtros
    filterset_class = ServicioFilter  # Asignar el filtro


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()  # Consulta todas las regiones
    serializer_class = RegionSerializer
  

class ServicioPrestacionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServicioPrestacion.objects.all()
    serializer_class = ServicioPrestacionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServicioPrestacionFilter  # Filtra prestaciones por el id del servicio

class ReseniaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resenia.objects.all()
    serializer_class = ReseniaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReseniaFilter  # Filtra reseñas por el id del servicio 

# Vista de Registro
@api_view(['POST'])
def register(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.create_user(username=username, password=password)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_201_CREATED)

# Vista de Inicio de Sesión
@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.get(username=username)
    if user.check_password(password):
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)