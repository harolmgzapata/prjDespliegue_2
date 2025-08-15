from django.shortcuts import render
from .models import Usuarios

# Create your views here.

def index(request):
    usuarios = Usuarios.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, 'render/index.html', contexto)
