from django.contrib import admin
from .models import Cancha, Reserva, Usuario



# Register your models here.
admin.site.register(Cancha)
admin.site.register(Usuario)
admin.site.register(Reserva)