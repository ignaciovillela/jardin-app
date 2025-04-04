from django.contrib import admin
from .models import Jardinero

@admin.register(Jardinero)
class JardineroAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'phone', 'is_active', 'hire_date')
    list_filter = ('specialty', 'is_active')
    search_fields = ('name',)
