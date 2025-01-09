<<<<<<< HEAD
"""
URL configuration for hotel_luna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

=======
>>>>>>> b37f1732 (Proyecto final: Hotel Luna)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD

urlpatterns = [
    # Ruta al panel de administración
    path('admin/', admin.site.urls),

    # Rutas para la aplicación de reservas
    path('', include('reservas.urls', namespace='reservas')),

    # Rutas para la aplicación de blog
    path('blog/', include('blog.urls', namespace='blog')),

    # Rutas para la aplicación de usuarios (login, registro, etc.)
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
]

# Configuración para servir archivos estáticos y multimedia en desarrollo
=======
from django.shortcuts import redirect

urlpatterns = [
    # ✅ Redirección automática a /admin/
    path('', lambda request: redirect('/admin/')),

    # ✅ Ruta al panel de administración
    path('admin/', admin.site.urls),

    # ✅ Rutas para la aplicación de reservas
    path('reservas/', include('reservas.urls', namespace='reservas')),

    # ✅ Rutas para la aplicación de blog
    path('blog/', include('blog.urls', namespace='blog')),

    # ✅ Rutas para la aplicación de usuarios (login, registro, etc.)
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
]

# ✅ Configuración para servir archivos estáticos y multimedia en desarrollo
>>>>>>> b37f1732 (Proyecto final: Hotel Luna)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
