from django import forms

from .models import Cita


class AsignarCitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['solicitud', 'jardinero', 'fecha_programada']
        widgets = {
            'fecha_programada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ConfirmarCitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = []

class CalificarCitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['calificacion', 'comentario']
        widgets = {
            'calificacion': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comentario': forms.Textarea(attrs={'rows': 3}),
        }
