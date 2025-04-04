from django.contrib import admin
from django.urls import path, include
from clientes.views import InicioView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('clientes/', include('clientes.urls')),
    path('servicios/', include('servicios.urls')),
    path('agenda/', include('agenda.urls')),
    path('admin/', admin.site.urls),
]
