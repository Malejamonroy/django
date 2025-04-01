from django.shortcuts import render
from .models import Historial

def index(request):
    historial = Historial.objects.filter(usuario=request.user)
    return render(request, 'usuarios/historial.html', {'historial': historial})
