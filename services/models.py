from django.contrib.auth.models import User
from django.db import models

class Region(models.Model):
    descripcion = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    idUsuario = models.ForeignKey(User, on_delete=models.PROTECT)        

class Comuna(models.Model):
    descripcion = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)           


class PrestadorCategoria(models.Model):
    descripcion = models.CharField(max_length=300)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT) 


class Prestador(models.Model):
    descripcion = models.CharField(max_length=300)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=0)
    categoria = models.ForeignKey(PrestadorCategoria, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    direccionCalle = models.CharField(max_length=100)
    direccionNumero = models.IntegerField(default=0)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)


class ServicioTipo(models.Model):
    descripcion = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(auto_now_add=True)


class Servicio(models.Model):
    descripcion = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=0)
    valor = models.IntegerField(default=0)
    tipo = models.ForeignKey(ServicioTipo, on_delete=models.PROTECT)    
    categoria = models.IntegerField(default=0)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)    
    prestador = models.ForeignKey(Prestador, on_delete=models.PROTECT)

class Prestacion(models.Model):
    descripcion = models.CharField(max_length=100)
    icono = models.CharField(max_length=100)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=1)    
    
class ServicioPrestacion(models.Model):
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE) 
    prestacion = models.ForeignKey('Prestacion', on_delete=models.CASCADE) 
    tipo = models.CharField(max_length=2) # PR = principal / AD = adicional
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(default=1)



# Modelo de Reseña
class Resenia(models.Model):
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)  # Relación con el servicio
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que dejó la reseña
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating de 1 a 5
    comentario = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña por {self.usuario.username} - {self.rating} estrellas"