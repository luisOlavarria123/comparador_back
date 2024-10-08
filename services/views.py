from rest_framework import viewsets
from .models import Servicio, Review
from .serializers import ServiceSerializer, ReviewSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ServicioFilter

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]  # Habilitar el backend de filtros
    filterset_class = ServicioFilter  # Asignar el filtro

# Vista para Reseñas
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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