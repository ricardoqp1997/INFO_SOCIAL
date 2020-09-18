# Librerías de Django para el manejo de las vistas, plantillas y navegación
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Módulos para la manipulación de usuarios
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

# Módulos de forms.py
from .forms import (
    UserLoginForm,
)


# redireccionamiento de la pagina respecto a la autenticación del usuario
def index(request):
    if request.user.is_authenticated:
        return redirect('main/')
    else:
        logout(request)
        return redirect('login/')


# Vista de inicio de sesión

def login_view(request):

    form = UserLoginForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/main/')

    login_context = {
        'form': form,
        'page_title': 'Inicio de sesión'
    }

    return render(request, 'login.html', login_context)


# Vista de acceso a portal principal (Hola mundo en primer prueba)

@login_required
def main(request):
    return render(request, 'main.html')
