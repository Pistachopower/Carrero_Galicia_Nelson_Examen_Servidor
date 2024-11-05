from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, unique=True)
    direccion = models.TextField(null=True, blank=True)

    


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    anio_estreno = models.IntegerField()
    usuario = models.ManyToManyField(Usuario, through='Alquiler', related_name="peliculas_alquiladas")
    voto = models.ManyToManyField(Usuario, through='Voto', related_name="peliculas_votadas")


class Alquiler(models.Model):
    fecha_alquiler = models.DateTimeField(default=timezone.now)
    fecha_entrega = models.DateTimeField(null=True, blank=True)  # Permitir nulos temporalmente
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name="alquileres")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="alquileres_usuario")



class Voto(models.Model):
    PUNTUACION_CHOICES = [
        ('1', 'Uno'),
        ('2', 'Dos'),
        ('3', 'Tres'),
        ('4', 'Cuatro'),
        ('5', 'Cinco'),
    ]
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name="votos")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="votos_usuario")
    puntuacion = models.CharField(max_length=1, choices=PUNTUACION_CHOICES)
    comentario = models.TextField()
    fecha_hora = models.DateTimeField(default=timezone.now)



class CuentaBancaria(models.Model):
    BANCO_CHOICES = [
        ('Caixa', 'Caixa'),
        ('BBVA', 'BBVA'),
        ('UNICAJA', 'Unicaja'),
        ('ING', 'ING'),
    ]
    numero_cuenta = models.CharField(max_length=20)
    banco = models.CharField(max_length=8, choices=BANCO_CHOICES)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="cuenta_bancaria")

