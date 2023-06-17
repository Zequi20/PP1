from django.db import models

# Create your models here.
class Empleado(models.Model):
    identificador = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=150, null=False)
    departamento = models.CharField(max_length=100, null=False)
    fecha_inicio = models.DateField(auto_now_add=True)
    dias_trabajo = models.CharField(max_length=100, null=False)
    TURNO_OPCIONES = (
        ('dia', 'Día'),
        ('tarde', 'Tarde'),
        ('noche', 'Noche'),
    )
    turno = models.CharField(max_length=10, choices=TURNO_OPCIONES, null=False)
    horario_entrada = models.TimeField(null=False)
    horario_salida = models.TimeField(null=False)


class Jornada(models.Model):
    identificador = models.CharField(max_length=50, unique=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,  null=False)
    fecha = models.DateTimeField(null=False)
    TIPO_MARCACION = (
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    )
    tipo_marcacion = models.CharField(max_length=10, choices=TIPO_MARCACION, null=False)

  

