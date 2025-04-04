from django.db import models

class Jardinero(models.Model):
    SPECIALTIES = [
        ('pruning', 'Poda experta'),
        ('design', 'Diseño paisajístico'),
        ('maintenance', 'Mantenimiento integral'),
        ('irrigation', 'Sistemas de riego'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nombre")
    specialty = models.CharField(max_length=50, choices=SPECIALTIES, verbose_name="Especialidad")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    email = models.EmailField(blank=True, verbose_name="Correo electrónico")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    hire_date = models.DateField(auto_now_add=True, verbose_name="Fecha de contratación")

    def __str__(self):
        return f"{self.name} ({self.get_specialty_display()})"

    class Meta:
        verbose_name = "Jardinero"
        verbose_name_plural = "Jardineros"
