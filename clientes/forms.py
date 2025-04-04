from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente, Solicitud


class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=30)
    last_name = forms.CharField(label="Apellido", max_length=30)
    phone = forms.CharField(label="Teléfono", max_length=20)
    address = forms.CharField(label="Dirección", widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            Cliente.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address']
            )
        return user


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        exclude = ['cliente', 'created_at']
        widgets = {
            'availability': forms.TextInput(attrs={'placeholder': 'Ej: Lunes a Viernes 9:00-18:00'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
