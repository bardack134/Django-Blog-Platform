"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# Importa las funciones y configuraciones necesarias de Django para administrar la aplicación.
from django.contrib import admin
from django.urls import path, include

# Importa el módulo utilizado para trabajar con archivos estáticos y el directorio especificado en STATICFILES_DIRS.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Importa la configuración global del proyecto Django desde settings.py.
from django.conf import settings

# Lista de patrones de URL para el enrutamiento de la aplicación.
urlpatterns = [
    # Ruta para acceder al panel de administración de Django.
    path('admin/', admin.site.urls),
    
    # Ruta principal que incluye las URL definidas en el archivo main.urls.
    path('', include('main.urls'))
]

# Agrega las URL para el manejo de archivos estáticos.
urlpatterns += staticfiles_urlpatterns()
