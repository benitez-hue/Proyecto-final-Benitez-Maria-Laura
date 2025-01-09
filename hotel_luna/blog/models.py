from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Autor")
    fecha_publicacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Publicación")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")

    def __str__(self):
        return self.titulo

