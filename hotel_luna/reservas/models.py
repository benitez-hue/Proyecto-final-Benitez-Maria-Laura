from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError


# Modelo de Habitación
class Habitacion(models.Model):
    TIPO_HABITACION = [
        ('Doble_Estandar', 'Doble Estándar'),
        ('Doble_Superior', 'Doble Superior'),
        ('Single_Estandar', 'Single Estándar'),
        ('Single_Superior', 'Single Superior'),
    ]

    TEMPORADA_CHOICES = [
        ('Verano', 'Verano'),
        ('Invierno', 'Invierno'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_HABITACION, verbose_name="Tipo de Habitación")
    numero = models.IntegerField(unique=True, verbose_name="Número de Habitación")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    temporada = models.CharField(max_length=10, choices=TEMPORADA_CHOICES, verbose_name="Temporada")

    def __str__(self):
        return f"Habitación {self.numero} - {self.get_tipo_display()} ({self.temporada})"

    def esta_disponible(self, fecha_entrada, fecha_salida):
        """
        Verifica si la habitación está disponible para un rango de fechas específico.
        """
        reservas_activas = self.reserva_set.filter(
            estado='Confirmada',
            fecha_entrada__lt=fecha_salida,
            fecha_salida__gt=fecha_entrada
        )
        return not reservas_activas.exists()

    class Meta:
        verbose_name = "Habitación"
        verbose_name_plural = "Habitaciones"


# Modelo de Reserva
class Reserva(models.Model):
    ESTADO_RESERVA = [
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada'),
        ('Pendiente', 'Pendiente'),
    ]

    TEMPORADA_CHOICES = [
        ('Verano', 'Verano'),
        ('Invierno', 'Invierno'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, verbose_name="Habitación")
    fecha_entrada = models.DateField(verbose_name="Fecha de Entrada")
    fecha_salida = models.DateField(verbose_name="Fecha de Salida")
    estado = models.CharField(max_length=20, choices=ESTADO_RESERVA, default='Pendiente', verbose_name="Estado de la Reserva")
    temporada = models.CharField(max_length=10, choices=TEMPORADA_CHOICES, verbose_name="Temporada")

    def __str__(self):
        return f"Reserva de {self.usuario.username} - Habitación {self.habitacion.numero} ({self.estado}) - {self.temporada}"

    def clean(self):
        """
        Validación de fechas antes de guardar la reserva.
        """
        if self.fecha_entrada >= self.fecha_salida:
            raise ValidationError("La fecha de entrada debe ser anterior a la fecha de salida.")

    def save(self, *args, **kwargs):
        """
        Llama a clean() antes de guardar el objeto.
        """
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"


# Modelo de Búsqueda Laboral
class BusquedaLaboral(models.Model):
    puesto = models.CharField(max_length=100, verbose_name="Puesto")
    descripcion = models.TextField(verbose_name="Descripción")
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Salario")
    fecha_publicacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Publicación")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")

    def __str__(self):
        return f"{self.puesto} - {'Disponible' if self.disponible else 'No disponible'}"

    def es_actual(self):
        """
        Retorna True si la oferta fue publicada en los últimos 30 días.
        """
        return (date.today() - self.fecha_publicacion).days <= 30

    class Meta:
        verbose_name = "Búsqueda Laboral"
        verbose_name_plural = "Búsquedas Laborales"
