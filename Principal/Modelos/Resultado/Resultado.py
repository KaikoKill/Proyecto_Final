from django.contrib.auth.models import User
from django.db import models
from Principal.Modelos.Convocatoria.Convocatoria import Convocatoria
from Principal.Modelos.Evento.Evento import Evento
from Principal.Modelos.Inscripcion.Inscripcion import Inscripcion

# Create your models here.
class Resultado(models.Model):
    inscripcion = models.ForeignKey(Inscripcion,on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=255)
    puntuacion = models.IntegerField()
    def __str__(self):
        return self.evento.nombre_evento
    def get_ubicacion(self):
        conv=Convocatoria.objects.get(evento=self.evento)
        return conv.ubicacion
       