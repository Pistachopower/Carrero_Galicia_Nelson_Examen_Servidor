from django.shortcuts import render
from django.db.models import Q, Count
from .models import Usuario, CuentaBancaria, Pelicula, Sistema_votacion

def index(request):
   return render(request, 'index.html')


def ultimoVoto(request):
   ult_voto= Sistema_votacion.objects.select_related('pelicula','usuario')
   ult_voto= ult_voto.order_by('-fechaHora')[:1]
   return render(request, 'ultimoVoto.html', {'ultimoVoto':ult_voto})


"""
Todos los modelos principales que tengan votos con una puntuación 
numérica menor a 3 y que realizó un usuario o cliente en concreto:
"""
def puntuacionmenor(request, id):
   puntuacion= Sistema_votacion.objects.select_related('pelicula','usuario')
   #usuario__id= id: haces esto para que funcione con el seeder
   puntuacion= puntuacion.filter(puntuacion__lt= 3).filter(usuario__id= id)
   return render(request, 'puntuacionmenor.html', {'puntuacionmenor':puntuacion})

"""
Todos los usuarios o clientes que no han votado nunca y mostrar información sobre 
estos usuarios y clientes al completo: 1.5 puntos
"""

def usuariosinvoto(request):
   #usuarios = Usuario.objects.all()
   sinvoto = Usuario.objects.annotate(num_votos=Count('sistema_votacion')).filter(num_votos=0)
   #sinvoto = usuarios.filter(sistema_votacion= None)
   return render(request, 'sinVoto.html', {'sinvoto':sinvoto})
 
  
"""
Obtener las cuentas bancarias que sean de la Caixa o de Unicaja y que el 
propietario tenga un nombre que contenga un texto en concreto, por ejemplo “Juan”: 
"""
def cuentasBancariasPropietario(request,propietario):
   cuentaBancariasP= CuentaBancaria.objects.select_related('usuario')
   cuentaBancariasP= cuentaBancariasP.filter(Q(banco= 'CAIXA') | 
                           Q(banco= 'UNICAJA')).filter(usuario__nombre__contains= propietario)
   return render(request, 'cuentasBancariasPropietario.html', {'cuentasbancariaspropietario':cuentaBancariasP})


"""
Obtener los votos de los usuarios que hayan votado a partir del 2023 con una puntuación 
numérica igual a 5  y que tengan asociada una cuenta bancaria. 
"""
#def votosUsuario2023puntuacion(request):
#   usuarioVotoCuenta= Usuario.objects.select_related('CuentaBancaria_Usuario').prefetch_related('sistema_votacion')
#   #usuarios_queryset = Usuario.objects.select_related('CuentaBancaria_Usuario').prefetch_related('sistema_votacion_set')
#   return render(request, 'votosUsuario2023puntuacion.html', {'usuarioVotoCuenta':usuarioVotoCuenta})

def votosUsuario2023puntuacion(request):
    # Filtrar usuarios que tienen una cuenta bancaria asociada y cuyos votos cumplen las condiciones
    usuarioVotoCuenta = Usuario.objects.filter(
        CuentaBancaria_Usuario__isnull=False,  # Verifica que tengan cuenta bancaria asociada
        sistema_votacion__fechaHora__year__gte=2023,  # Filtra los votos a partir del año 2023
        sistema_votacion__puntuacion=5  # Verifica que la puntuación sea igual a 5
    ).select_related('CuentaBancaria_Usuario').prefetch_related('sistema_votacion_set')

    return render(request, 'votosUsuario2023puntuacion.html', {'usuarioVotoCuenta': usuarioVotoCuenta})