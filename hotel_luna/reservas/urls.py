from django.urls import path
from . import views

# Definimos el espacio de nombres para las rutas de la app "reservas"
app_name = 'reservas'

urlpatterns = [
    # ✅ Ruta para la página principal
    path('', views.home, name='home'),

    # ✅ Rutas para las páginas de temporada
    path('verano/', views.verano, name='verano'),
    path('invierno/', views.invierno, name='invierno'),

    # ✅ Ruta para el detalle de una reserva específica
    path('detalle/<int:id>/', views.detalle_reserva, name='detalle_reserva'),

    # ✅ Ruta para cancelar una reserva
    path('cancelar/<int:id>/', views.cancelar_reserva, name='cancelar_reserva'),

    # ✅ Ruta para ver la disponibilidad de habitaciones
    path('disponibilidad/', views.disponibilidad, name='disponibilidad'),

    # ✅ Ruta para la sección de búsqueda laboral
    path('busquedalaboral/', views.busqueda_laboral, name='busqueda_laboral'),

    # ✅ Ruta para hacer reservas online
    path('reserva_online/', views.reserva_online, name='reserva_online'),

    # ✅ Ruta para modificar una reserva existente
    path('modificar_reserva/<int:id>/', views.modificar_reserva, name='modificar_reserva'),

    # ✅ Ruta para ver el listado de reservas realizadas
    path('listado_reservas/', views.listado_reservas, name='listado_reservas'),
]
