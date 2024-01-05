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


# Importa la función 'static' para manejar archivos estáticos y multimedia
from django.conf.urls.static import static

# Importa la configuración global del proyecto Django desde settings.py.
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Lista de patrones de URL para el enrutamiento de la aplicación.
urlpatterns = [
    # Ruta para acceder al panel de administración de Django.
    path('admin/', admin.site.urls),
    
    # Ruta principal que incluye las URL definidas en el archivo main.urls.
    path('', include('main.urls'))
]

urlpatterns += staticfiles_urlpatterns()
# # Configuración para servir archivos estáticos y multimedia durante el desarrollo
# if settings.DEBUG:
#     # Agrega las URL para servir archivos multimedia (MEDIA_URL) usando la ruta del sistema de archivos especificada en MEDIA_ROOT
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
