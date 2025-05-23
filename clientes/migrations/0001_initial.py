# Generated by Django 5.2 on 2025-04-04 17:54

import django.core.validators
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
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Teléfono de contacto')),
                ('address', models.TextField(verbose_name='Dirección completa')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('pruning', 'Poda de árboles/arbustos'), ('design', 'Diseño de jardín'), ('maintenance', 'Mantenimiento general'), ('irrigation', 'Instalación de riego')], max_length=50, verbose_name='Tipo de servicio')),
                ('description', models.TextField(blank=True, verbose_name='Detalles adicionales')),
                ('square_meters', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Metros cuadrados')),
                ('availability', models.CharField(help_text='Ej: Lunes a Viernes 9:00-18:00', max_length=100, verbose_name='Disponibilidad horaria')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Latitud')),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Longitud')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='clientes.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Solicitud de servicio',
                'verbose_name_plural': 'Solicitudes de servicio',
                'ordering': ['-created_at'],
            },
        ),
    ]
