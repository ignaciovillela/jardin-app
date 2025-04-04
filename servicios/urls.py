from django.urls import path
from .views import (
    ListaJardinerosView,
    CrearJardineroView,
    EditarJardineroView,
    EliminarJardineroView
)

urlpatterns = [
    path('', ListaJardinerosView.as_view(), name='lista_jardineros'),
    path('crear/', CrearJardineroView.as_view(), name='crear_jardinero'),
    path('editar/<int:pk>/', EditarJardineroView.as_view(), name='editar_jardinero'),
    path('eliminar/<int:pk>/', EliminarJardineroView.as_view(), name='eliminar_jardinero'),
]
