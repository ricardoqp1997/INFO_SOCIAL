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


from django.contrib import admin
from django.urls import path
from portal_web import views as portal_views

# URLs del portal web
urlpatterns = [

    # index de "portal_web" redireccionará a Login si no se ha iniciado sesión
    path('', portal_views.index, name='index'),

    path('login/', portal_views.login, name='login'),

    # Acceso al panel administrativo
    path('admin/', admin.site.urls),
]
