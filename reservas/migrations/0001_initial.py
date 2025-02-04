# Generated by Django 5.1.4 on 2025-01-07 19:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Doble_Estandar', 'Doble Estándar'), ('Doble_Superior', 'Doble Superior'), ('Single_Estandar', 'Single Estándar'), ('Single_Superior', 'Single Superior')], max_length=20)),
                ('numero', models.IntegerField(unique=True)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('estado', models.CharField(choices=[('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')], max_length=20)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.habitacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
