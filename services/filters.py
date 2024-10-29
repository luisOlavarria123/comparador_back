import django_filters
from .models import Servicio, ServicioPrestacion, Resenia

class ServicioFilter(django_filters.FilterSet):
    # Filtro para un conjunto de IDs de regiones
    comunas = django_filters.BaseInFilter(field_name="prestador__comuna__id", lookup_expr='in')
    
    # Filtro para el precio máximo
    precio_max = django_filters.NumberFilter(field_name="valor", lookup_expr='lte')

    class Meta:
        model = Servicio
        fields = ['comunas', 'precio_max']  # Añadimos los filtros personalizados

    @property
    def qs(self):
        # Obtener el queryset original
        queryset = super().qs
        
        # Verificar si el filtro de comunas está vacío
        if not self.data.get('comunas'):
            # Si el filtro de regiones está vacío, devolver un queryset vacío
            return queryset.none()

        # Si hay regiones, devolver el queryset filtrado normalmente
        return queryset
    

class ServicioPrestacionFilter(django_filters.FilterSet):
    servicio_id = django_filters.NumberFilter(field_name='servicio__id', lookup_expr='exact')

    class Meta:
        model = ServicioPrestacion
        fields = ['servicio_id']

class ReseniaFilter(django_filters.FilterSet):
    servicio_id = django_filters.NumberFilter(field_name='servicio__id', lookup_expr='exact')

    class Meta:
        model = Resenia
        fields = ['servicio_id']    