from django.contrib import admin
from .Modelos.Evento.Evento import Evento
from .Modelos.Usuario.Usuario import Usuario
from .Modelos.Convocatoria.Convocatoria import Convocatoria
from .Modelos.Inscripcion.Inscripcion import Inscripcion
from .Modelos.Resultado.Resultado import Resultado



#Register your models here.

admin.site.register(Evento)
admin.site.register(Convocatoria)
admin.site.register(Usuario)
admin.site.register(Inscripcion)
admin.site.register(Resultado)
