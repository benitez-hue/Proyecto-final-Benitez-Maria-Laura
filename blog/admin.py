from django.contrib import admin
from .models import Blog

# Registrar el modelo Blog en el panel de administración
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'disponible')
    search_fields = ('titulo', 'autor__username')
    list_filter = ('disponible', 'fecha_publicacion')
