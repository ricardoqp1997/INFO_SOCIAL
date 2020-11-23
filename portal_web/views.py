# Librerías de Django para el manejo de las vistas, plantillas y navegación
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Módulos de configuracion del proyecto
from django.conf import settings

# Módulos para la manipulación de usuarios
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from django.contrib.auth.models import Group

# Módulos de forms.py
from .forms import (
    UserLoginForm,
)

from .models import *

user = None


# redireccionamiento de la pagina respecto a la autenticación del usuario
def index(request):
    if request.user.is_authenticated:
        return redirect('/main/')
    else:
        logout(request)
        return redirect('login/')


# redireccionamiento de la pagina al portal administrativo
def redirect_admin(request):
    return redirect('/admin/')


# Vista de inicio de sesión

def login_view(request):

    global user

    form = UserLoginForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/main/')

    login_context = {
        'form': form,
        'page_title': 'Inicio de sesión',

    }

    return render(request, 'login.html', login_context)


# Vista de acceso a portal principal (Hola mundo en primer prueba)

@login_required(login_url=settings.LOGIN_URL)
def main(request):

    if request.user.is_authenticated:

        global user
        tipo_usuario = Group.objects.get(user=request.user).name
        # print(request.user.username)
        # print('tipo_usuario: ' + str(tipo_usuario))

        context_inicio = {
            'Title': 'Inicio',
            'tipo_usuario': tipo_usuario
        }
        return render(request, 'main.html', context_inicio)
    else:
        return redirect('/login/')


@login_required(login_url=settings.LOGIN_URL)
def contenido_estudiante(request):

    asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=request.user).count()

    context_contenido = {
        'Title': 'Aula de clases',
        'on_screen': 'tablero',
        'subjects': asignaturas
    }
    return render(request, 'site_content.html', context_contenido)
