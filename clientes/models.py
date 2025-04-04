from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    phone = models.CharField(max_length=20, verbose_name="Teléfono de contacto")
    address = models.TextField(verbose_name="Dirección completa")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Solicitud(models.Model):
    SERVICE_TYPES = [
        ('pruning', 'Poda de árboles/arbustos'),
        ('design', 'Diseño de jardín'),
        ('maintenance', 'Mantenimiento general'),
        ('irrigation', 'Instalación de riego'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='solicitudes',
        verbose_name="Cliente"
    )
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES, verbose_name="Tipo de servicio")
    description = models.TextField(blank=True, verbose_name="Detalles adicionales")
    square_meters = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(1)],
        verbose_name="Metros cuadrados"
    )
    availability = models.CharField(
        max_length=100,
        verbose_name="Disponibilidad horaria",
        help_text="Ej: Lunes a Viernes 9:00-18:00"
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name="Latitud"
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name="Longitud"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def __str__(self):
        return f"Solicitud #{self.id} - {self.get_service_type_display()}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Solicitud de servicio"
        verbose_name_plural = "Solicitudes de servicio"
