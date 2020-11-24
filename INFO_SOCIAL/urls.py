"""INFO_SOCIAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from portal_web import views as portal_views
from django.contrib.auth import views as auth_views

# URLs del portal web
urlpatterns = [

    # Index de "portal_web" redireccionará a Login si no se ha iniciado sesión
    path('', portal_views.index, name='index'),

    # Manejo de sesión del usuario
    path('login/', portal_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    # Panel principal
    path('main/', portal_views.main, name='main'),

    # Accesos principales al sitio
    path('main/aula/', portal_views.contenido_estudiante, name='aula'),
    path('main/aula/', portal_views.contenido_estudiante, name='tareas'),
    path('main/aula/', portal_views.contenido_estudiante, name='resolucion_tareas'),

    path('main/docencia/', portal_views.contenido_docente, name='docencia'),
    path('main/noticias/', portal_views.main, name='noticias'),
    path('main/soporte/', portal_views.main, name='soporte'),

    # Acceso al panel administrativo
    path('admin-redirect/', portal_views.redirect_admin, name='administrador'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
