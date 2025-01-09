"""
URL configuration for hotel_luna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Ruta para el panel de administración
    path('admin/', admin.site.urls),

    # Ruta para la aplicación de reservas
    path('', include('reservas.urls', namespace='reservas')),

    # Ruta para la aplicación de blog
    path('blog/', include('blog.urls', namespace='blog')),

    # Ruta para la aplicación de usuarios
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
]

# Configuración para archivos estáticos y multimedia
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
