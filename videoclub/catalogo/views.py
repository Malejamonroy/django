from django.shortcuts import render
from .models import Pelicula

def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'catalogo/index.html', {'peliculas': peliculas})
