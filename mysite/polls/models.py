import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=80)
    telefono = models.CharField(max_length=20)
    clave = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    def __str__(self):
        return self.nombre

class Cancha(models.Model):
    deporte = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    inicio = models.TimeField()
    fin = models.TimeField()
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    aceptado = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)


