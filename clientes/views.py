from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic import TemplateView

from .forms import RegistroForm, SolicitudForm
from .models import Solicitud


class InicioView(TemplateView):
    template_name = 'inicio.html'


class RegistroView(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'clientes/registro.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class SolicitarVisitaView(LoginRequiredMixin, CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'clientes/solicitar_visita.html'
    success_url = reverse_lazy('lista_solicitudes_cliente')

    def form_valid(self, form):
        form.instance.cliente = self.request.user.cliente
        return super().form_valid(form)


class ListaSolicitudesClienteView(LoginRequiredMixin, ListView):
    model = Solicitud
    template_name = 'clientes/lista_solicitudes.html'
    context_object_name = 'solicitudes'

    def get_queryset(self):
        return Solicitud.objects.filter(cliente=self.request.user.cliente)


class DetalleSolicitudView(LoginRequiredMixin, DetailView):
    model = Solicitud
    template_name = 'clientes/detalle_solicitud.html'
    context_object_name = 'solicitud'

    def get_queryset(self):
        return Solicitud.objects.filter(cliente=self.request.user.cliente)
