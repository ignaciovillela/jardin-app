from django.urls import path
from .views import ListaCitasView, AsignarCitaView, ConfirmarCitaView, DetalleCitaView, CalificarCitaView

urlpatterns = [
    path('', ListaCitasView.as_view(), name='lista_citas'),
    path('asignar/', AsignarCitaView.as_view(), name='asignar_cita'),
    path('confirmar/<int:pk>/', ConfirmarCitaView.as_view(), name='confirmar_cita'),
    path('detalle/<int:pk>/', DetalleCitaView.as_view(), name='detalle_cita'),
    path('calificar/<int:pk>/', CalificarCitaView.as_view(), name='calificar_cita'),
]
