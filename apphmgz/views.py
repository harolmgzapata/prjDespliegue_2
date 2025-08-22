from django.shortcuts import render
from .models import Usuarios
from random import randint

# Create your views here.

def index(request):
    usuario = Usuarios()
    usr = str(randint(1000, 9999))
    correo = f"{usr}@correo.com"
    usuario.usuario = usr
    usuario.correo = correo
    usuario.clave = '1234'
    usuario.save()
    usuarios = Usuarios.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, 'render/index.html', contexto)
