import django_filters
from .models import Servicio

class ServicioFilter(django_filters.FilterSet):
    # Filtro para un conjunto de IDs de regiones
    regiones = django_filters.BaseInFilter(field_name="prestador__region__id", lookup_expr='in')
    
    # Filtro para el precio máximo
    precio_max = django_filters.NumberFilter(field_name="valor", lookup_expr='lte')

    class Meta:
        model = Servicio
        fields = ['regiones', 'precio_max']  # Añadimos los filtros personalizados