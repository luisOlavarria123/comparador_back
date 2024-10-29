from django.contrib import admin
from .models import Region, Comuna, Prestador, Servicio, PrestadorCategoria, ServicioTipo, Prestacion,ServicioPrestacion,Resenia

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')
    readonly_fields = ("fechaCreacion",)

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')
    readonly_fields = ("fechaCreacion",)

class PrestadorCategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')
    readonly_fields = ("fechaCreacion",)

class PrestadorAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')
    readonly_fields = ("fechaCreacion",)


class ServicioTipoAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion')
    readonly_fields = ("fechaCreacion",)

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','prestador_descripcion')
    readonly_fields = ("fechaCreacion",)            
    def prestador_descripcion(self, obj):
        return obj.prestador.descripcion
    prestador_descripcion.short_description = 'prestador_descripcion'

class PrestacionAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','icono','estado')
    readonly_fields = ("fechaCreacion",)        
    
class ServicioPrestacionAdmin(admin.ModelAdmin):
    list_display = ('id','servicio','prestacion')
    readonly_fields = ("fechaCreacion",)            
    def prestacion_descripcion(self, obj):
        return obj.prestacion.descripcion
    prestacion_descripcion.short_description = 'prestacion'
    def servicio_descripcion(self, obj):
        return obj.servicio.descripcion
    servicio_descripcion.short_description = 'servicio'

class ReseniaAdmin(admin.ModelAdmin):
    list_display = ('id','servicio_descripcion','usuario_nombre','rating','comentario','fechaCreacion')
    readonly_fields = ("fechaCreacion",)    
    def servicio_descripcion(self, obj):
        return obj.servicio.descripcion
    servicio_descripcion.short_description = 'servicio_descripcion'    
    def usuario_nombre(self, obj):
        return obj.usuario.username
    servicio_descripcion.short_description = 'usuario_nombre'        

admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(PrestadorCategoria, PrestadorCategoriaAdmin)
admin.site.register(Prestador, PrestadorAdmin)

admin.site.register(ServicioTipo, ServicioTipoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Prestacion, PrestacionAdmin)
admin.site.register(ServicioPrestacion, ServicioPrestacionAdmin)
admin.site.register(Resenia, ReseniaAdmin)
