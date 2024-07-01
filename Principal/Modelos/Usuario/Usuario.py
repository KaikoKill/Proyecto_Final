from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Usuario(User):
    es_estudiante = models.BooleanField()
    sexo = models.CharField(max_length=255, null=True)
    edad = models.IntegerField(null=True) 

    def __str__(self):
        return self.username