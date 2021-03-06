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
from django.contrib.auth.decorators import login_required

from django.contrib import admin
from django.urls import path

from blog_colegio.views import (
    BlogList,
    BlogDetail
)

from portal_web import views as portal_views
from django.contrib.auth import views as auth_views
from portal_web.views import (
    ListaClases,
    ListaTareas,
    DetalleClases,
    DetalleTareas,
    ResolverTareas
)

admin.site.site_header = "Tu Colegio a Distancia"
admin.site.site_title = "Tu Colegio a Distancia"
admin.site.index_title = "Bienvenido al portal administrativo"

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
    path('main/aula/curso/', portal_views.panel_curso, name='curso'),
    path('main/aula/contacto-y-soporte/', portal_views.panel_asignaturas, name='asignaturas'),

    # Clases
    path('main/aula/lecciones', login_required(ListaClases.as_view(), login_url=settings.LOGIN_URL), name='contenido_clases'),
    path('main/aula/leccion/<int:pk>', login_required(DetalleClases.as_view(), login_url=settings.LOGIN_URL), name='detalle_clase'),

    # Tareas
    path('main/aula/tareas', login_required(ListaTareas.as_view(), login_url=settings.LOGIN_URL), name='tareas_pendientes'),
    path('main/aula/tarea/<int:assigment_pk>', login_required(ResolverTareas.as_view(), login_url=settings.LOGIN_URL), name='resolucion_tareas'),
    path('main/aula/tarea-resuelta/<int:pk>', login_required(DetalleTareas.as_view(), login_url=settings.LOGIN_URL), name='vista_tareas_resueltas'),

    # Redireccionamiento de docentes
    path('main/docencia/', portal_views.contenido_docente, name='docencia'),

    # Blog
    path('main/noticias/', login_required(BlogList.as_view(), login_url=settings.LOGIN_URL), name='noticias'),
    path('main/noticias/<int:pk>', login_required(BlogDetail.as_view(), login_url=settings.LOGIN_URL), name='noticia'),

    # Acceso al panel administrativo
    path('admin-redirect/', portal_views.redirect_admin, name='administrador'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
