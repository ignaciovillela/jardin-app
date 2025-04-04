from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Jardinero
from .forms import JardineroForm
from django.contrib.auth.mixins import UserPassesTestMixin

class EsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class ListaJardinerosView(EsAdminMixin, ListView):
    model = Jardinero
    template_name = 'servicios/lista_jardineros.html'
    context_object_name = 'jardineros'

class CrearJardineroView(EsAdminMixin, CreateView):
    model = Jardinero
    form_class = JardineroForm
    template_name = 'servicios/form_jardinero.html'
    success_url = reverse_lazy('lista_jardineros')

class EditarJardineroView(EsAdminMixin, UpdateView):
    model = Jardinero
    form_class = JardineroForm
    template_name = 'servicios/form_jardinero.html'
    success_url = reverse_lazy('lista_jardineros')

class EliminarJardineroView(EsAdminMixin, DeleteView):
    model = Jardinero
    template_name = 'servicios/confirmar_eliminar_jardinero.html'
    success_url = reverse_lazy('lista_jardineros')
