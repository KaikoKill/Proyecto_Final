from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from Principal.Modelos.Convocatoria.Convocatoria import Convocatoria
from Principal.Modelos.Inscripcion.Inscripcion import Inscripcion
from Principal.Modelos.Usuario.Usuario import Usuario


class Ver_Inscripciones(LoginRequiredMixin ,UserPassesTestMixin,ListView):
    model = Inscripcion
    template_name = 'Inscripciones/Ver_Inscripciones.html'  
    context_object_name = 'incri'
      
    def get_queryset(self):
        return Inscripcion.objects.all()
    
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return reverse_lazy('login')    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        return context
   

class Gestionar_Inscripciones(LoginRequiredMixin ,UserPassesTestMixin,ListView):
    model = Inscripcion
    template_name = 'Inscripciones/Gestionar_Inscripciones.html'  
    context_object_name = 'incri'
      
    def get_queryset(self):
        return Inscripcion.objects.all()
    
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return reverse_lazy('login')    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        context['users'] = Usuario.objects.all()
        context['conv'] = Convocatoria.objects.all()
        return context

class Solicitud_Inscripciones(LoginRequiredMixin ,UserPassesTestMixin,ListView):
    model = Inscripcion
    template_name = 'Inscripciones/Solicitud_Inscripciones.html'  
    context_object_name = 'incri'
      
    def get_queryset(self):
        return Inscripcion.objects.all()
    
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return reverse_lazy('login')    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        return context 

class Enviar_InscripcionCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Inscripcion
    template_name = 'Convocatorias/Ver_Convocatorias.html'
    fields = ['convocatoria','nombre_equipo', 'usuario','integrante1', 'integrante2','integrante3']
    success_url = reverse_lazy('Ver_Inscripciones')
    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance                                   
        # Check if a Convocatoria with the same name already exists (excluding current instance)
        existing_equipo = Inscripcion.objects.filter(nombre_equipo=instance.nombre_equipo).exclude(pk=instance.pk).exists()    
        if existing_equipo:
            # If there's an existing convocatoria with the same name, return an error
            form.add_error('nombre_equipo', 'Ya existe un equipo con ese nombre.')
            return self.form_invalid(form)

        # Assign the event to the instance         
        user_id = form.cleaned_data.get('user_id')
        conv_id = form.cleaned_data.get('conv_id')
        print(instance)
        if user_id and conv_id:
            usuario = Usuario.objects.get(pk=user_id)
            convocatoria = Convocatoria.objects.get(pk=conv_id)
            instance.usuario = usuario
            instance.convocatoria = convocatoria   
            instance.save()    
        return super().form_valid(form)          

    def get_queryset(self):
        return Usuario.objects.all()        
    def test_func(self):
        return self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        return context    

class Editar_InscripcionUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Inscripcion
    template_name = 'Convocatorias/Ver_Convocatorias.html'
    fields = ['convocatoria','nombre_equipo', 'usuario','integrante1', 'integrante2','integrante3']
    success_url = reverse_lazy('Ver_Inscripciones')
    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance                                   
        # Check if a Convocatoria with the same name already exists (excluding current instance)
        existing_equipo = Inscripcion.objects.filter(nombre_equipo=instance.nombre_equipo).exclude(pk=instance.pk).exists()    
        if existing_equipo:
            # If there's an existing convocatoria with the same name, return an error
            form.add_error('nombre_equipo', 'Ya existe un equipo con ese nombre.')
            return self.form_invalid(form)

        # Assign the event to the instance         
        user_id = form.cleaned_data.get('user_id')
        conv_id = form.cleaned_data.get('conv_id')
        print(instance)
        if user_id and conv_id:
            usuario = Usuario.objects.get(pk=user_id)
            convocatoria = Convocatoria.objects.get(pk=conv_id)
            instance.usuario = usuario
            instance.convocatoria = convocatoria   
            instance.save()    
        return super().form_valid(form)          
     
    def test_func(self):
        return self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('login')
    
class Agregar_InscripcionCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Inscripcion
    template_name = 'Inscripciones/Gestionar_Inscripciones.html'
    fields = ['convocatoria','nombre_equipo', 'usuario','integrante1', 'integrante2','integrante3']
    success_url = reverse_lazy('Gestionar_Inscripciones')
    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance                                   
        # Check if a Convocatoria with the same name already exists (excluding current instance)
        existing_equipo = Inscripcion.objects.filter(nombre_equipo=instance.nombre_equipo).exclude(pk=instance.pk).exists()    
        if existing_equipo:
            # If there's an existing convocatoria with the same name, return an error
            form.add_error('nombre_equipo', 'Ya existe un equipo con ese nombre.')
            return self.form_invalid(form)

        # Assign the event to the instance         
        user_id = form.cleaned_data.get('user_id')
        conv_id = form.cleaned_data.get('conv_id')
        if user_id and conv_id:
            usuario = Usuario.objects.get(pk=user_id)
            convocatoria = Convocatoria.objects.get(pk=conv_id)
            instance.usuario = usuario
            instance.convocatoria = convocatoria   
            instance.save()    
        return super().form_valid(form)          

    def get_queryset(self):
        return Usuario.objects.all()        
    def test_func(self):
        return self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        return context  
    
class Modificar_InscripcionUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Inscripcion
    template_name = 'Inscripciones/Gestionar_Inscripciones.html'
    fields = ['convocatoria','nombre_equipo', 'usuario','integrante1', 'integrante2','integrante3', 'estado']
    success_url = reverse_lazy('Gestionar_Inscripciones')
    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance                                   
        # Check if a Convocatoria with the same name already exists (excluding current instance)
        existing_equipo = Inscripcion.objects.filter(nombre_equipo=instance.nombre_equipo).exclude(pk=instance.pk).exists()    
        if existing_equipo:
            # If there's an existing convocatoria with the same name, return an error
            form.add_error('nombre_equipo', 'Ya existe un equipo con ese nombre.')
            return self.form_invalid(form)

        # Assign the event to the instance         
        user_id = form.cleaned_data.get('user_id')
        conv_id = form.cleaned_data.get('conv_id')
        if user_id and conv_id:
            usuario = Usuario.objects.get(pk=user_id)
            convocatoria = Convocatoria.objects.get(pk=conv_id)
            instance.usuario = usuario
            instance.convocatoria = convocatoria   
            instance.save()    
        return super().form_valid(form)          
     
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('login')

class Eliminar_Inscripcion(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Inscripcion
    template_name = 'Inscripciones/Gestionar_Inscripciones.html'
    success_url = reverse_lazy('Gestionar_Inscripciones')

    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')    

    
class IncriUserDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Inscripcion
    template_name = 'Inscripciones/Ver_Inscripciones.html'
    success_url = reverse_lazy('Ver_Inscripciones')

    def test_func(self):
        return self.request.user.is_authenticated
    def handle_no_permission(self):
        return redirect('login')
    

class Aceptar_Inscripcion(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Inscripcion
    template_name = 'Inscripciones/Solicitud_Inscripciones.html'
    success_url = reverse_lazy('Solicitud_Inscripciones')
    fields = ['estado']
   
   
    def form_valid(self, form):
        instance = form.instance
        instance.save()    
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')

class Denegar_Inscripcion(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Inscripcion
    template_name = 'Inscripciones/Solicitud_Inscripciones.html'
    success_url = reverse_lazy('Solicitud_Inscripciones')
    fields = ['estado']
   
   
    def form_valid(self, form):
        instance = form.instance
        instance.save()    
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')