from django.contrib import admin
# Register your models here.
from .models import Usuario, Pelicula, Alquiler, Voto, CuentaBancaria
admin.site.register(Usuario)
admin.site.register(Pelicula)
admin.site.register(Alquiler)
admin.site.register(Voto)
admin.site.register(CuentaBancaria)