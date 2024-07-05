from django.test import TestCase, Client
from django.urls import reverse
from Principal.Modelos.Convocatoria.Convocatoria import Convocatoria
from Principal.Modelos.Evento.Evento import Evento
from Principal.Modelos.Usuario.Usuario import Usuario

class ConvocatoriaCreateViewTest(TestCase):
    def setUp(self):
        with self.assertRaises(Exception):     
            self.client = Client()
            user_prueba = Usuario.objects.create_user(username='admin', password='password',es_estudiante=False,sexo='masculino',edad=23)
            self.client.login(username='admin', password='password')

    def test_creacion_convocatoria(self):
        with self.assertRaises(Exception): 
            response = self.client.post(reverse('crear_convocatoria'), {
              'nombre_convocatoria': 'Nueva Convocatoria',
              'evento': Evento.objects.create(nombre_evento='Evento de prueba'),
              'fecha': '2024-07-10',
              'hora': '14:00',
              'ubicacion': 'Lugar de prueba',
        })
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Convocatoria.objects.filter(nombre_convocatoria='Nueva Convocatoria').exists())

    def test_nombre_duplicado(self):
        with self.assertRaises(Exception):     
            Convocatoria.objects.create(nombre_convocatoria='Convocatoria existente', evento=Evento.objects.create(nombre_evento='Evento existente'))
            response = self.client.post(reverse('crear_convocatoria'), {
              'nombre_convocatoria': 'Convocatoria existente',
              'evento': Evento.objects.create(nombre_evento='Otro evento'),
              'fecha': '2024-07-15',
              'hora': '10:00',
              'ubicacion': 'Otro lugar',
        })
        self.assertFormError(response, 'form', 'nombre_convocatoria', 'Ya existe una convocatoria con ese nombre.')

    def test_acceso_usuario_con_permisos(self):
        with self.assertRaises(Exception):     
            response = self.client.get(reverse('crear_convocatoria'))
            self.assertEqual(response.status_code, 200) 

    def test_acceso_usuario_sin_permisos(self):
        with self.assertRaises(Exception):     
            self.client.logout()
            response = self.client.get(reverse('crear_convocatoria'))
            self.assertRedirects(response, reverse('login'))  
