from django.contrib import admin
from .models import Cliente, Solicitud


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'phone', 'address')

    def username(self, obj):
        return obj.user.username

    def full_name(self, obj):
        return obj.user.get_full_name()


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_type', 'cliente', 'created_at')
    list_filter = ('service_type',)
    search_fields = ('cliente__user__username',)
