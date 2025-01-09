from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Habitacion, Reserva, BusquedaLaboral
from datetime import date
from .forms import ReservaForm


# ✅ Vista para la página principal
def home(request):
    return render(request, 'reservas/home.html')


# ✅ Vista para la temporada de verano
def verano(request):
    return render(request, 'reservas/verano.html')


# ✅ Vista para la temporada de invierno
def invierno(request):
    return render(request, 'reservas/invierno.html')


# ✅ Vista para el detalle de una reserva
def detalle_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {
        'reserva': reserva,
        'cliente_nombre': reserva.usuario.username,
        'tipo_habitacion': reserva.habitacion.get_tipo_display(),
        'fecha_entrada': reserva.fecha_entrada,
        'fecha_salida': reserva.fecha_salida,
        'estado': reserva.estado,
    }
    return render(request, 'reservas/detalle.html', context)


# ✅ Vista para cancelar una reserva
def cancelar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if reserva.estado != 'Cancelada':
        reserva.estado = 'Cancelada'
        reserva.save()
        messages.success(request, 'La reserva ha sido cancelada correctamente.')
    else:
        messages.info(request, 'La reserva ya estaba cancelada.')
    return redirect('reservas:home')


# ✅ Vista para la disponibilidad de habitaciones por temporada y fechas
def disponibilidad(request):
    temporada = request.GET.get('temporada', 'Verano')  # Verano por defecto
    fecha_entrada = request.GET.get('fecha_entrada', str(date.today()))
    fecha_salida = request.GET.get('fecha_salida', str(date.today()))

    if fecha_entrada >= fecha_salida:
        messages.error(request, 'La fecha de entrada debe ser anterior a la fecha de salida.')
        return render(request, 'reservas/disponibilidad.html', {})

    habitaciones = Habitacion.objects.filter(temporada=temporada).exclude(
        reserva__estado='Confirmada',
        reserva__fecha_entrada__lt=fecha_salida,
        reserva__fecha_salida__gt=fecha_entrada
    )

    context = {
        'temporada': temporada,
        'fecha_entrada': fecha_entrada,
        'fecha_salida': fecha_salida,
        'habitaciones': habitaciones,
    }
    return render(request, 'reservas/disponibilidad.html', context)


# ✅ Vista para realizar reservas online
def reserva_online(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            if reserva.habitacion.esta_disponible(reserva.fecha_entrada, reserva.fecha_salida):
                reserva.estado = 'Confirmada'
                reserva.save()
                messages.success(request, 'Reserva realizada con éxito.')
                return redirect('reservas:listado_reservas')
            else:
                messages.error(request, 'La habitación no está disponible para las fechas seleccionadas.')
    else:
        form = ReservaForm()

    return render(request, 'reservas/reserva_online.html', {'form': form})


# ✅ Vista para modificar una reserva existente
def modificar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva modificada con éxito.')
            return redirect('reservas:detalle_reserva', id=reserva.id)
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'reservas/modificar_reserva.html', {'form': form, 'reserva': reserva})


# ✅ Vista para el listado de reservas
def listado_reservas(request):
    reservas = Reserva.objects.all().order_by('-fecha_entrada')
    return render(request, 'reservas/listado_reservas.html', {'reservas': reservas})


# ✅ Vista para mostrar las búsquedas laborales disponibles
def busqueda_laboral(request):
    ofertas = BusquedaLaboral.objects.filter(disponible=True)
    return render(request, 'reservas/busquedalaboral.html', {'ofertas': ofertas})
