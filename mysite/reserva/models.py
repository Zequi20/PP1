from django.db import models

# Create your models here.
class Hotel(models.Model):
    id = models.SmallIntegerField(primary_key= True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

class Reserva(models.Model):
    id = models.IntegerField(primary_key= True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    cant_huespedes = models.SmallIntegerField()
    tipo_habitacion = models.CharField(max_length=5)
    precio_total = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=5)
