from rest_framework import serializers
from .models import Servicio, Resenia, Comuna, Region,ServicioPrestacion, Prestacion

class ServicioSerializer(serializers.ModelSerializer):

    prestador_nombre = serializers.CharField(source='prestador.descripcion', read_only=True)
    region_nombre = serializers.CharField(source='prestador.region.descripcion', read_only=True)
    comuna_nombre = serializers.CharField(source='prestador.comuna.descripcion', read_only=True)
    direccionCalle = serializers.CharField(source='prestador.direccionCalle', read_only=True)
    direccionNumero = serializers.CharField(source='prestador.direccionNumero', read_only=True)
    

    class Meta:
        model = Servicio
        fields = ['id', 'descripcion', 'valor', 'prestador_nombre','region_nombre','comuna_nombre','direccionCalle','direccionNumero']  


class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id', 'descripcion']

class RegionSerializer(serializers.ModelSerializer):
    comunas = ComunaSerializer(many=True, read_only=True)
    class Meta:
        model = Region
        fields = ['id', 'descripcion','comunas']        


class PrestacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestacion
        fields = ['id', 'descripcion', 'icono', 'estado']

class ServicioPrestacionSerializer(serializers.ModelSerializer):
    prestacion = PrestacionSerializer(read_only=True)

    class Meta:
        model = ServicioPrestacion
        fields = ['prestacion', 'tipo', 'estado']

class ReseniaSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = Resenia
        fields = ['usuario_nombre', 'rating', 'comentario', 'fechaCreacion']        