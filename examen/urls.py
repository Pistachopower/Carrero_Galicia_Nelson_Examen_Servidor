from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('voto_usuario_pelicula', views.ultimo_voto, name='voto_usuario_pelicula'),
    path('usuariosprincipales/<int:usuario_id>', views.usuariosprincipales, name='puntuacion_numerica'),
    path('peliculas-media-votacion/', views.peliculas_con_media_votacion, name='peliculas_media_votacion'),
    path('votos-usuario-banco/', views.votos_usuario_banco, name='votos_usuario_banco'),

    ]

