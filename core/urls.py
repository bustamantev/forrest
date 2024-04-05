from django.urls import path
from .views import menuprincipal_wiki, animales, armas, construcciones, consumibles, enemigos, flora, forowiki, historia, inicio_sesion_wiki, logros, lugarestf, micuentatf, recuperarcontra, registrase_wiki

urlpatterns = [
    path('', menuprincipal_wiki,name="menuprincipal_wiki"),
    path('Animales.html', animales,name="Animales"),
    path('Armas.html', armas,name="Armas"),
    path('Construcciones.html', construcciones,name="Construcciones"),
    path('Consumibles.html', consumibles,name="Consumibles"),
    path('Enemigos.html', enemigos,name="Enemigos"),
    path('Flora.html', flora,name="Flora"),
    path('forowiki.html', forowiki,name="forowiki"),
    path('historia.html', historia,name="historia"),
    path('inicio_sesion_wiki.html', inicio_sesion_wiki,name="inicio_sesion_wiki"),
    path('Logros.html', logros,name="Logros"),
    path('Lugarestf.html', lugarestf,name="Lugarestf"),
    path('micuentatf.html', micuentatf,name="micuentatf"),
    path('recuperarcontra.html', recuperarcontra,name="recuperarcontra"),
    path('registrase_wiki.html', registrase_wiki,name="registrase_wiki"),

    
]
