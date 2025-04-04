from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    RegistroView, SolicitarVisitaView, ListaSolicitudesClienteView,
    DetalleSolicitudView,
)


urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(template_name='clientes/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('solicitar/', SolicitarVisitaView.as_view(), name='solicitar_visita'),
    path('mis-solicitudes/', ListaSolicitudesClienteView.as_view(), name='lista_solicitudes_cliente'),
    path('solicitud/<int:pk>/', DetalleSolicitudView.as_view(), name='detalle_solicitud'),
]
