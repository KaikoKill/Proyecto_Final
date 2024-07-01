from django import forms
from django.contrib.auth.forms import UserCreationForm
from Principal.Modelos.Evento.Evento import Evento

class EventoModelForm(forms.ModelForm):

  class Meta:
    model = Evento
    fields = ('nombre_evento', 'descripcion', 'requisitos')
    
    
    
class EventoUpdateModelForm(forms.ModelForm):

  class Meta:
    model = Evento
    fields = ('nombre_evento', 'descripcion', 'requisitos')
