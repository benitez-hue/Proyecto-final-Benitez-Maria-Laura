from django.contrib import admin
from .models import Habitacion, Reserva, BusquedaLaboral

# Registra los modelos en el panel de administración
admin.site.register(Habitacion)
admin.site.register(Reserva)
admin.site.register(BusquedaLaboral)
