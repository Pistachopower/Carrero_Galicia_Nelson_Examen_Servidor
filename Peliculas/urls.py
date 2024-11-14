from django.urls import path
from .import views


urlpatterns = [
   path('', views.index, name='index'),
   path('ultimovoto',views.ultimoVoto,name='ultimoVoto'),
   path('puntuacionmenor/<int:id>',views.puntuacionmenor,name='puntuacionmenor'),
   path('usuariosinvoto',views.usuariosinvoto,name='usuariosinvoto'),
   path('cuentasbancariaspropietario/<str:propietario>',views.cuentasBancariasPropietario,name='cuentasbancariaspropietario'),
   path('votosUsuario2023puntuacion',views.votosUsuario2023puntuacion,name='usuarioVotoCuenta'),
]
