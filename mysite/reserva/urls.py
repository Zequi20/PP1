from django.urls import path

from . import views

app_name = "reserva"

urlpatterns = [
    path('reserva/all/', views.listado_reservas, name='listado_reservas'),
]