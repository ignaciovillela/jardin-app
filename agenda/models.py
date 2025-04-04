from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

class Cita(models.Model):
    ESTADOS = [
        ('pending', 'Pendiente de confirmación'),
        ('confirmed', 'Confirmada'),
        ('completed', 'Completada'),
        ('canceled', 'Cancelada'),
    ]

    solicitud = models.OneToOneField(
        'clientes.Solicitud',
        on_delete=models.CASCADE,
        related_name='cita',
        verbose_name="Solicitud"
    )
    jardinero = models.ForeignKey(
        'servicios.Jardinero',
        on_delete=models.SET_NULL,
        null=True,
        related_name='citas',
        verbose_name="Jardinero"
    )
    fecha_programada = models.DateTimeField(verbose_name="Fecha programada")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pending', verbose_name="Estado")
    notas = models.TextField(blank=True, verbose_name="Notas", help_text="Observaciones internas")
    calificacion = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Calificación",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="De 1 a 5 estrellas"
    )
    comentario = models.TextField(blank=True, verbose_name="Comentario", help_text="Comentario del cliente")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def __str__(self):
        return f"Cita #{self.id} - {self.solicitud.cliente.user.username}"

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        indexes = [
            models.Index(fields=['fecha_programada']),
        ]
