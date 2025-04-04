from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Cita
from .forms import AsignarCitaForm, ConfirmarCitaForm, CalificarCitaForm
from clientes.models import Solicitud


class ListaCitasView(LoginRequiredMixin, ListView):
    model = Cita
    template_name = 'agenda/lista_citas.html'
    context_object_name = 'citas'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Cita.objects.all().order_by('-fecha_programada')
        return Cita.objects.filter(solicitud__cliente__user=self.request.user).order_by('-fecha_programada')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_admin'] = self.request.user.is_superuser
        return context


class AsignarCitaView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Cita
    form_class = AsignarCitaForm
    template_name = 'agenda/asignar_cita.html'
    success_url = reverse_lazy('lista_citas')

    def test_func(self):
        return self.request.user.is_superuser

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Solo mostrar solicitudes que no tengan cita asignada
        form.fields['solicitud'].queryset = Solicitud.objects.filter(cita__isnull=True)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solicitudes'] = Solicitud.objects.all()
        return context


class ConfirmarCitaView(LoginRequiredMixin, UpdateView):
    model = Cita
    form_class = ConfirmarCitaForm
    template_name = 'agenda/confirmar_cita.html'
    success_url = reverse_lazy('lista_citas')

    def get_queryset(self):
        # Solo permitir confirmar citas propias
        return Cita.objects.filter(solicitud__cliente__user=self.request.user, estado='pending')

    def form_valid(self, form):
        form.instance.estado = 'confirmed'
        return super().form_valid(form)


class DetalleCitaView(LoginRequiredMixin, DetailView):
    model = Cita
    template_name = 'agenda/detalle_cita.html'
    context_object_name = 'cita'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Cita.objects.all()
        return Cita.objects.filter(solicitud__cliente__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_admin'] = self.request.user.is_superuser
        context['estados_disponibles'] = ['pending', 'confirmed', 'completed', 'canceled']
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user.is_superuser:
            nuevo_estado = request.POST.get('nuevo_estado')
            if nuevo_estado in dict(Cita.ESTADOS).keys():
                self.object.estado = nuevo_estado
                self.object.save()
        return self.get(request, *args, **kwargs)


class CalificarCitaView(LoginRequiredMixin, UpdateView):
    model = Cita
    form_class = CalificarCitaForm
    template_name = 'agenda/calificar_cita.html'
    success_url = reverse_lazy('lista_citas')

    def get_queryset(self):
        return Cita.objects.filter(
            solicitud__cliente__user=self.request.user,
            estado='completed',
            calificacion__isnull=True
        )
