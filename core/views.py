from django.shortcuts import render

# Create your views here.

def animales(request):
    return render(request, 'core/Animales.html')

def armas(request):
    return render(request, 'core/Armas.html')

def construcciones(request):
    return render(request, 'core/Construcciones.html')

def consumibles(request):
    return render(request, 'core/Consumibles.html')

def enemigos(request):
    return render(request, 'core/Enemigos.html')

def flora(request):
    return render(request, 'core/Flora.html')

def forowiki(request):
    return render(request, 'core/forowiki.html')

def historia(request):
    return render(request, 'core/historia.html')

def inicio_sesion_wiki(request):
    return render(request, 'core/inicio_sesion_wiki.html')

def logros(request):
    return render(request, 'core/Logros.html')

def lugarestf(request):
    return render(request, 'core/Lugarestf.html')

def menuprincipal_wiki(request):
    return render(request, 'core/menuprincipal_wiki.html')

def micuentatf(request):
    return render(request, 'core/micuentatf.html')

def recuperarcontra(request):
    return render(request, 'core/recuperarcontra.html')

def registrase_wiki(request):
    return render(request, 'core/registrase_wiki.html')
