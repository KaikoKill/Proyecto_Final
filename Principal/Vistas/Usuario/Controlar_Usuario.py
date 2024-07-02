from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from Principal.Modelos.Evento.Evento import Evento
from Principal.Modelos.Usuario.Usuario import Usuario
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Principal.Vistas.Usuario.forms import UsuarioModelForm, UsuarioUpdateModelForm
from django.contrib import messages

def error404(request):
    return render(request, "Usuarios/404.html")

#Vista que controla el Login 
class UserLoginView(LoginView):
    template_name = 'Usuarios/login.html'
    
    def get_success_url(self):
        
        user = self.request.user    
        if user.is_authenticated and (user.is_superuser or user.is_staff):
            if  User.objects.get(id = user.id).is_staff:
                return reverse_lazy('Principal')
        return reverse_lazy('Principal')
        
class Home(LoginRequiredMixin, TemplateView):
    login_url = 'Usuarios/login.html'
    
    def Principal(request):
        return render(request, "Usuarios/index.html")
    
    def get_queryset(self):
        return Usuario.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        context['eventos'] = Evento.objects.all()
        return context    
    
    
class Administrar_Permisos(LoginRequiredMixin ,UserPassesTestMixin,ListView):
    model = Usuario
    template_name = 'Usuarios/Administrar_Permisos.html'  
    context_object_name = 'users'
    paginate_by = 5
      
    def get_queryset(self):
        return Usuario.objects.all()
    
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return reverse_lazy('login')    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        return context    


#Vista que visualiza la lista de Usuarios 
class listUserView(LoginRequiredMixin ,UserPassesTestMixin,ListView):
    model = Usuario
    template_name = 'Usuarios/Gestionar_Usuarios.html'  
    context_object_name = 'users'
    paginate_by = 5
    
    def get_queryset(self):
        return Usuario.objects.all()
    
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        return context  

class UserCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Usuario
    template_name = 'Usuarios/Gestionar_Usuarios.html'
    form_class = UsuarioModelForm
    success_url = "/Gestionar_Usuarios/?created"
    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance
        # Check if is_jefe is being set to True
        if instance.es_estudiante:
            instance.is_staff = False
            # Check if there's another user in the same area who is a boss
            existing_user = User.objects.filter(username = instance.username ).exclude(pk=instance.pk).exists()
            if existing_user:
                # If there's an existing boss, return an error
                form.add_error('username', 'Ya existe un estudiante con ese nombre .')
                
                return self.form_invalid(form)
        else:
            instance.is_staff = True
            # Check if there's another user in the same area who is a boss
            existing_user = User.objects.filter(username = instance.username ).exclude(pk=instance.pk).exists()
            if existing_user:
                # If there's an existing boss, return an error
                form.add_error('username', 'Ya existe un Jefe de Departamento con ese nombre .')
                return self.form_invalid(form)
        # Call the parent class's form_valid method
        instance.save()

        return super().form_valid(form)
    

    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')
        

class UserUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Usuario
    template_name = 'Usuarios/Gestionar_Usuarios.html'
    form_class = UsuarioUpdateModelForm
    success_url = "/Gestionar_Usuarios/?edit"    
    
    
    def form_valid(self, form):
        instance = form.instance
        instance.set_password(form.cleaned_data['password'])  # Encriptar la contraseña antes de guardarla
        instance.save()
        return super().form_valid(form)
    
    
    def test_func(self):
        return self.request.user.is_staff 
    
    def handle_no_permission(self):
        return redirect('login')

class UserEditView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Usuario
    template_name = 'Usuarios/index.html'
    form_class = UsuarioUpdateModelForm
    success_url = reverse_lazy('login')    
   
    def form_valid(self, form):
        instance = form.instance
        instance.set_password(form.cleaned_data['password'])  # Encriptar la contraseña antes de guardarla
        instance.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('login')
    

    
class UserDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Usuario
    template_name = 'Usuarios/Gestionar_Usuarios.html'
    success_url = "/Gestionar_Usuarios/?delete" 

    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')

class Modificar_Permisos(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Usuario
    template_name = 'Usuarios/Administrar_Permisos.html'
    fields = ['es_estudiante']
    success_url = "/Administrar_Permisos/?edit"    
    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance
        # Check if is_jefe is being set to True
        if instance.es_estudiante:
            instance.is_staff = False
        else:
            instance.is_staff = True
        # Call the parent class's form_valid method
        instance.save()
        return super().form_valid(form)
        
    def test_func(self):
        return self.request.user.is_staff 
    
    def handle_no_permission(self):
        return redirect('login')
