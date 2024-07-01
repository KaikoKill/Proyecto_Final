from django.contrib.auth.models import User
from django.db import models
from Principal.Modelos.Convocatoria.Convocatoria import Convocatoria



# Create your models here.

class Inscripcion(models.Model):
    convocatoria = models.ForeignKey(Convocatoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_equipo = models.CharField(max_length=255)
    integrante1 = models.CharField(max_length=255)  
    integrante2 = models.CharField(max_length=255)
    integrante3 = models.CharField(max_length=255)
    estado = models.CharField(default = 'Esperando', max_length=255) 
    def __str__(self):
        return self.nombre_equipo
