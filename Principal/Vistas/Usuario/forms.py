from django import forms
from django.contrib.auth.forms import UserCreationForm
from Principal.Modelos.Usuario.Usuario import Usuario
from django.forms import ValidationError

class UsuarioModelForm(UserCreationForm):

  class Meta:
    model = Usuario
    fields = ('username', 'first_name', 'last_name', 'password1','password2','es_estudiante', 'sexo', 'email','edad')
    
    
class UsuarioUpdateModelForm(forms.ModelForm):

  class Meta:
    model = Usuario
    fields = ('username','first_name','password','last_name','sexo','email','edad')
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)  # Encriptar la contraseña antes de guardarla
        if commit:
            user.save()
        return user