from django.db import models

# Create your models here.

class Evento(models.Model):
    nombre_evento = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    requisitos = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre_evento
