from rest_framework import serializers
from .models import Servicio, Review

class ServiceSerializer(serializers.ModelSerializer):

    prestador_nombre = serializers.CharField(source='prestador.descripcion', read_only=True)
    region_nombre = serializers.CharField(source='prestador.region.descripcion', read_only=True)
    comuna_nombre = serializers.CharField(source='prestador.comuna.descripcion', read_only=True)
    direccionCalle = serializers.CharField(source='prestador.direccionCalle', read_only=True)
    direccionNumero = serializers.CharField(source='prestador.direccionNumero', read_only=True)
    

    class Meta:
        model = Servicio
        fields = ['id', 'descripcion', 'valor', 'prestador_nombre','region_nombre','comuna_nombre','direccionCalle','direccionNumero']  

# Serializador de Reseña
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'