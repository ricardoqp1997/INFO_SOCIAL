# Librerías de Django para el manejo de las vistas, plantillas y navegación
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView
)

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
def contenido_docente(request):
    return redirect('/admin/')


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

    tipo_usuario = Group.objects.get(user=request.user).name

    try:
        asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=request.user)
        cant_asignaturas = asignaturas.count()
    except:
        cant_asignaturas = asignaturas = None

    try:
        tareas = Tarea.objects.filter(
            estudiante__user_id=request.user.id,
            estado=Tarea.ENVIADA
        )
        cant_tareas = tareas.count()
        list_tareas = tareas[:5]
    except:
        list_tareas = cant_tareas = tareas = None

    try:
        clases = Clase.objects.filter(
            estudiante__user_id=request.user.id
        )
        cant_clases = clases.count()
        list_clases = clases[:5]
    except:
        list_clases = cant_clases = clases = None

    context_contenido = {
        'Title': 'Aula de clases',
        'tipo_usuario': tipo_usuario,
        'on_screen': 'tablero',

        'subjects_count': cant_asignaturas,
        'tasks_count': cant_tareas,
        'classes_count': cant_clases,

        'tasks_list': list_tareas,
        'classes_list': list_clases,
    }

    return render(request, 'dashboard.html', context_contenido)


def panel_curso(request):

    tipo_usuario = Group.objects.get(user=request.user).name

    try:
        asignaturas = Asignatura.objects.filter(curso__estudiante__user_id=request.user)
        cant_asignaturas = asignaturas.count()
    except:
        cant_asignaturas = asignaturas = None

    try:
        tareas = Tarea.objects.filter(
            estudiante__user_id=request.user.id,
            estado=Tarea.ENVIADA
        )
        cant_tareas = tareas.count()
        list_tareas = tareas[:5]
    except:
        list_tareas = cant_tareas = tareas = None

    try:
        clases = Clase.objects.filter(
            estudiante__user_id=request.user.id
        )
        cant_clases = clases.count()
        list_clases = clases[:5]
    except:
        list_clases = cant_clases = clases = None

    try:
        partners = Estudiante.objects.filter(
            curso__estudiante__user_id=request.user.id
        )
        print(partners)
    except:
        partners = None

    context_contenido = {
        'Title': 'Aula de clases',
        'tipo_usuario': tipo_usuario,
        'on_screen': 'curso',

        'subjects_count': cant_asignaturas,
        'tasks_count': cant_tareas,
        'classes_count': cant_clases,

        'tasks_list': list_tareas,
        'classes_list': list_clases,
        'partners_list': partners,
    }

    return render(request, 'curso.html', context_contenido)


class ListaTareas(ListView):
    pass


class ListaClases(ListView):
    pass


class DetalleTareas(ListView):
    pass


class DetalleClases(ListView):
    pass
