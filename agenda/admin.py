from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'solicitud', 'jardinero', 'fecha_programada', 'estado')
    list_filter = ('estado', 'fecha_programada')
    search_fields = ('solicitud__cliente__name', 'jardinero__name')
    autocomplete_fields = ['solicitud', 'jardinero']
