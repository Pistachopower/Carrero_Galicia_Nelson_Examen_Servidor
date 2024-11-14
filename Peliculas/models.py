from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)


class CuentaBancaria(models.Model):
    numero_Cuenta= models.CharField(max_length=100) 
    BANCO = [
    	("CAIXA", "CAIXA"),
    	("BBVA", "BBVA"),
    	("UNICAJA", "UNICAJA"),
    	("ING", "ING"),
	]
    banco= models.CharField(max_length=10,choices=BANCO)
    usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, related_name="CuentaBancaria_Usuario")


class Pelicula(models.Model):
    nombre= models.CharField(max_length=100)
    categoria= models.CharField(max_length=100)
    cantidad_Actores= models.IntegerField(null = True)
    usuario= models.ManyToManyField(Usuario, through='Sistema_votacion')

#tabla intermedia
class Sistema_votacion(models.Model):
    puntuacion= models.IntegerField(null = True)
    comentario= models.CharField(max_length=100)
    fechaHora= models.DateTimeField(default=timezone.now)
    pelicula= models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)





    
    





