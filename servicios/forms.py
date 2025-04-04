from django import forms
from .models import Jardinero

class JardineroForm(forms.ModelForm):
    class Meta:
        model = Jardinero
        fields = ['name', 'specialty', 'phone', 'email', 'is_active']
