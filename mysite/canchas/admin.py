from django.contrib import admin
from .models import Cancha, Reserva, Usuario

class CanchaAdmin(admin.ModelAdmin):
    # List display: Qué campos mostrar en la lista de objetos
    list_display = ('nombre', 'deporte', 'direccion', 'telefono')

    # List filter: Qué campos usar para filtrar en la lista
    list_filter = ['direccion', 'deporte']

    # Search fields: Qué campos se usarán en la búsqueda
    search_fields = ('nombre', 'deporte', 'direccion')

    # Date hierarchy: Jerarquía de fechas para navegar por la lista

class UsuarioAdmin(admin.ModelAdmin):
    # List display: Qué campos mostrar en la lista de objetos
    list_display = ('nombre', 'correo', 'telefono', 'direccion')

    # List filter: Qué campos usar para filtrar en la lista
    list_filter = ['direccion']

    # Search fields: Qué campos se usarán en la búsqueda
    search_fields = ('nombre', 'correo', 'telefono', 'direccion')

class ReservaAdmin(admin.ModelAdmin):
    # List display: Qué campos mostrar en la lista de objetos
    list_display = ('usuario', 'cancha', 'fecha','precio', 'aceptado')

    # List filter: Qué campos usar para filtrar en la lista
    list_filter = ['aceptado', 'usuario']
    list_editable = ['precio', 'aceptado']
    # Search fields: Qué campos se usarán en la búsqueda
    search_fields = ('usuario', 'cancha', 'fecha','precio', 'aceptado')

# Register your models here.
admin.site.register(Cancha, CanchaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Reserva, ReservaAdmin)