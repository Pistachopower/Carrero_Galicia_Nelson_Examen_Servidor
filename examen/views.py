from django.shortcuts import render
from .models import Usuario, Pelicula, Alquiler, Voto, CuentaBancaria
from django.db.models import Avg, Max, Min, Prefetch

# Create your views here.
def index(request):
    return render(request,'index.html')


"""
El último voto que se realizó en un modelo principal en concreto, y
mostrar el comentario, la votación e información del usuario o cliente 
que lo realizó

"""
def ultimo_voto(request):
    voto_usuario_pelicula= Voto.objects.prefetch_related('pelicula', 'usuario')
    return render(request, 'voto_usuario_pelicula.html', {'voto_usuario_pelicula':voto_usuario_pelicula})


"""
Todos los modelos principales que tengan votos con una puntuación numérica menor a 3 y que realizó 
un usuario o cliente en concreto
"""
def usuariosprincipales(request, usuario_id):
    # filtra los votos con puntuación menor a 3 y realizados por el usuario especificado
    peliculas_filtradas = Pelicula.objects.filter(votos__puntuacion__='3', votos__usuario_id=usuario_id
    ).distinct()

    return render(request, 'peliculas_filtradas.html', {'peliculas_filtradas': peliculas_filtradas})


def peliculas_con_media_votacion(request):
    # obtener películas con una media de votaciones mayor a 2.5
    peliculas = Pelicula.objects.annotate(
        media_votacion=Avg('votos__puntuacion')
    ).filter(media_votacion__gt=2.5)
    
    return render(request, 'peliculas_media_votacion.html', {'peliculas': peliculas})



def votos_usuario_banco(request):
    # Obtener votos de usuarios con puntuación 5 a partir de 2023 y que tienen cuenta bancaria
    votos = Voto.objects.filter(
        puntuacion='5',
        fecha_hora__year__gte=2023,
        usuario__cuentaBancaria_Usuario__isnull=False
    ).select_related('usuario', 'pelicula')
    
    return render(request, 'votos_usuario_banco.html', {'votos': votos})


