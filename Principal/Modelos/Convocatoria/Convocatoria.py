from django.db import models

# Create your models here.
from Principal.Modelos.Evento.Evento import Evento

class Convocatoria(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nombre_convocatoria = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_convocatoria

