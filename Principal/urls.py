from django.urls import path
from .Vistas.Convocatoria import Controlar_Convocatoria
from .Vistas.Evento import Controlar_Evento
from .Vistas.Inscripcion import Controlar_Inscripcion
from .Vistas.Usuario import Controlar_Usuario
from .Vistas.Resultado import Controlar_Resultado

urlpatterns = [

    path('', Controlar_Usuario.UserLoginView.as_view(template_name= 'Usuarios/login.html'), name= "login"),
    path('Principal/', Controlar_Usuario.Home.as_view(template_name = 'Usuarios/index.html'), name= "Principal"),
    path('error404/', Controlar_Usuario.error404, name= "error404"),
    
    path('Gestionar_Usuarios/', Controlar_Usuario.listUserView.as_view(template_name='Usuarios/Gestionar_Usuarios.html'), name= "Gestionar_Usuarios"),
    path('Crear_Usuario/', Controlar_Usuario.UserCreateView.as_view(template_name='Usuarios/Gestionar_Usuarios.html'), name="Crear_Usuario"),
    path('Modificar_Usuario/<int:pk>', Controlar_Usuario.UserUpdateView.as_view(template_name='Usuarios/Gestionar_Usuarios.html'), name="Modificar_Usuario"),
    path('Editar_Usuario/<int:pk>', Controlar_Usuario.UserEditView.as_view(template_name='base.html'), name="Editar_Usuario"),
    path('Eliminar_Usuario/<int:pk>', Controlar_Usuario.UserDeleteView.as_view(template_name='Usuarios/Gestionar_Usuarios.html'), name="Eliminar_Usuario"),
    
    path('Administrar_Permisos/', Controlar_Usuario.Administrar_Permisos.as_view(template_name = 'Usuarios/Administrar_Permisos.html'), name= "Administrar_Permisos"),
    path('Administrar_Permisos/<int:pk>', Controlar_Usuario.Modificar_Permisos.as_view(template_name='Usuarios/Administrar_Permisos.html'), name="Modificar_Permisos"),
 
    path('Gestionar_Eventos/', Controlar_Evento.Gestionar_Eventos.as_view(), name= "Gestionar_Eventos"),
    path('Crear_Evento/', Controlar_Evento.EventoCreateView.as_view(template_name='Eventos/Gestionar_Eventos.html'), name="Crear_Evento"),
    path('Modificar_Evento/<int:pk>', Controlar_Evento.EventoUpdateView.as_view(template_name='Eventos/Gestionar_Eventos.html'), name="Modificar_Evento"),
    path('Eliminar_Evento/<int:pk>', Controlar_Evento.EventoDeleteView.as_view(template_name='Eventos/Gestionar_Eventos.html'), name="Eliminar_Evento"),
    
    path('Gestionar_Convocatorias/', Controlar_Convocatoria.Gestionar_Convocatorias.as_view(), name= "Gestionar_Convocatorias"),
    path('Crear_Convocatoria/', Controlar_Convocatoria.ConvocatoriaCreateView.as_view(template_name='Convocatorias/Gestionar_Convocatorias.html'), name="Crear_Convocatoria"),
    path('Modificar_Convocatoria/<int:pk>', Controlar_Convocatoria.ConvocatoriaUpdateView.as_view(template_name='Convocatorias/Gestionar_Convocatorias.html'), name="Modificar_Convocatoria"),
    path('Eliminar_Convocatoria/<int:pk>', Controlar_Convocatoria.ConvocatoriaDeleteView.as_view(template_name='Convocatorias/Gestionar_Convocatorias.html'), name="Eliminar_Convocatoria"),
    
    path('Ver_Convocatorias/', Controlar_Convocatoria.Ver_Convocatorias.as_view(), name= "Ver_Convocatorias"),
    
    path('Solicitud_Inscripciones/', Controlar_Inscripcion.Solicitud_Inscripciones.as_view(),name='Solicitud_Inscripciones'),
    path('Gestionar_Inscripciones/', Controlar_Inscripcion.Gestionar_Inscripciones.as_view(),name='Gestionar_Inscripciones'),
    path('Ver_Inscripciones/', Controlar_Inscripcion.Ver_Inscripciones.as_view(), name= "Ver_Inscripciones"),
    path('Agregar_Inscripcion/',Controlar_Inscripcion.Agregar_InscripcionCreateView.as_view(template_name='Inscripciones/Gestionar_Inscripciones.html'), name= "Agregar_Inscripcion"),
    path('Modificar_Inscripcion/<int:pk>',Controlar_Inscripcion.Modificar_InscripcionUpdateView.as_view(template_name='Inscripciones/Gestionar_Inscripciones.html'), name= "Modificar_Inscripcion"),
    path('Eliminar_Inscripcion/<int:pk>',Controlar_Inscripcion.Eliminar_Inscripcion.as_view(template_name='Inscripciones/Gestionar_Inscripciones.html'), name= "Eliminar_Inscripcion"),
    
    path('Enviar_Inscripcion/',Controlar_Inscripcion.Enviar_InscripcionCreateView.as_view(template_name='Convocatorias/Ver_Convocatorias.html'), name= "Enviar_Inscripcion"),
    path('Aceptar_Inscripcion/<int:pk>',Controlar_Inscripcion.Aceptar_Inscripcion.as_view(template_name='Inscripciones/Solicitud_Inscripciones.html'), name= "Aceptar_Inscripcion"),
    path('Denegar_Inscripcion/<int:pk>',Controlar_Inscripcion.Denegar_Inscripcion.as_view(template_name='Inscripciones/Solicitud_Inscripciones.html'), name= "Denegar_Inscripcion"),
    path('Editar_Inscripcion/<int:pk>',Controlar_Inscripcion.Editar_InscripcionUpdateView.as_view(template_name='Inscripciones/Ver_Inscripciones.html'), name= "Editar_Inscripcion"),
    path('Borrar_Inscripcion/<int:pk>',Controlar_Inscripcion.IncriUserDeleteView.as_view(template_name='Inscripciones/Ver_Inscripciones.html'), name= "Borrar_Inscripcion"),
    
    path('Gestionar_Resultados/', Controlar_Resultado.Gestionar_Resultados.as_view(), name= "Gestionar_Resultados"),
    path('Ver_Resultados/', Controlar_Resultado.Ver_Resultados.as_view(), name= "Ver_Resultados"),
    path('Agregar_Resultado/',Controlar_Resultado.Agregar_Resultado.as_view(template_name='Resultados/Gestionar_Resultados.html'), name= "Agregar_Resultado"),
    path('Modificar_Resultado/<int:pk>',Controlar_Resultado.Modificar_Resultado.as_view(template_name='Resultados/Gestionar_Resultados.html'), name= "Modificar_Resultado"),
    path('Eliminar_Resultado/<int:pk>',Controlar_Resultado.Eliminar_Resultado.as_view(template_name='Resultados/Gestionar_Resultados.html'), name= "Eliminar_Resultado"),
    
]
