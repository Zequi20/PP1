from django.contrib import admin
from .models import Empleado, Jornada

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'departamento', 'turno']
    list_filter = ['nombre']
    ordering = ['-turno']
class JornadaAdmin(admin.ModelAdmin):
    list_display = ['empleado', 'fecha', 'tipo_marcacion']
    ordering = ['-fecha']

admin.site.register(Jornada, JornadaAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
