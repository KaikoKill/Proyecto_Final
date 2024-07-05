from django.db import IntegrityError
from django.test import TestCase
from Principal.Modelos.Evento.Evento import Evento
from Principal.Modelos.Convocatoria.Convocatoria import Convocatoria

class EventoModelTest(TestCase):

   

    @classmethod
    def setUpTestData(cls):
        #Configurar objetos no modificados utilizados por todos los métodos de prueba
        Evento.objects.create( nombre_evento='ICPC', descripcion='nacional', requisitos='5 puntos IP')

    def test_nombre_evento(self):
        evento = Evento.objects.get(nombre_evento='ICPC')
        self.assertEqual(evento.descripcion, 'nacional')
        self.assertEqual(evento.requisitos, '5 puntos IP')
        
    def test_nombre_evento_label(self):
        evento=Evento.objects.get(id=1)
        field_label = evento._meta.get_field('nombre_evento').verbose_name
        self.assertEqual(field_label,'nombre_evento')

    def test_descripcion_label(self):
        evento=Evento.objects.get(id=1)
        field_label = evento._meta.get_field('descripcion').verbose_name
        self.assertEqual(field_label,'descripcion')

    def test_requisitos_label(self):
        evento=Evento.objects.get(id=1)
        field_label = evento._meta.get_field('requisitos').verbose_name
        self.assertEqual(field_label,'requisitos')

    def test_nombre_evento_max_length(self):
        evento=Evento.objects.get(id=1)
        max_length = evento._meta.get_field('nombre_evento').max_length
        self.assertEqual(max_length,40)

    def test_object_str(self):
        evento=Evento.objects.get(id=1)
        expected_object_name = '%s' % (evento.nombre_evento)
        self.assertEqual(expected_object_name,str(evento))

    def test_campos_obligatorios(self):
        with self.assertRaises(IntegrityError): 
            Evento.objects.create()

   
