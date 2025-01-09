from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Ruta para listar los blogs
    path('', views.lista_blogs, name='lista_blogs'),

    # Ruta para el detalle de un blog específico
    path('<int:id>/', views.detalle_blog, name='detalle_blog'),

    # Ruta para crear un nuevo blog
    path('nuevo/', views.nuevo_blog, name='nuevo_blog'),
]
