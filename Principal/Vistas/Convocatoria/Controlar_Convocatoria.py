from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from Principal.Modelos.Convocatoria.Convocatoria import Convocatoria
from Principal.Modelos.Evento.Evento import Evento
from Principal.Modelos.Usuario.Usuario import Usuario


class Ver_Convocatorias(LoginRequiredMixin ,UserPassesTestMixin,ListView):
    model = Convocatoria
    template_name = 'Convocatorias/Ver_Convocatorias.html'  
    context_object_name = 'conv'
      
    def get_queryset1(self):
        return Convocatoria.objects.all()
    
    def get_queryset2(self):
        return Usuario.objects.all()
    
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return reverse_lazy('login')    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        context['eventos'] = Evento.objects.all()
        return context    
class Gestionar_Convocatorias(LoginRequiredMixin ,UserPassesTestMixin,ListView):
    model = Convocatoria
    template_name = 'Convocatorias/Gestionar_Convocatorias.html'  
    context_object_name = 'conv'
      
    def get_queryset(self):
        return Convocatoria.objects.all()
    
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return reverse_lazy('login')    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        context['eventos'] = Evento.objects.all()
        return context    
    
class ConvocatoriaCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Convocatoria
    template_name = 'Convocatorias/Gestionar_Convocatorias.html'
    fields = ['nombre_convocatoria','evento','fecha', 'hora', 'ubicacion']
    success_url = reverse_lazy('Gestionar_Convocatorias')
    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance                                     
        # Check if a Convocatoria with the same name already exists (excluding current instance)
        existing_conv = Convocatoria.objects.filter(nombre_convocatoria=instance.nombre_convocatoria).exclude(pk=instance.pk).exists()
        
        if existing_conv:
            # If there's an existing convocatoria with the same name, return an error
            form.add_error('nombre_convocatoria', 'Ya existe una convocatoria con ese nombre.')
            return self.form_invalid(form)

        # Assign the event to the instance
        evento_id = form.cleaned_data.get('evento_id')
        if evento_id:
            evento = Evento.objects.get(pk=evento_id)
            instance.evento = evento
            instance.save()              
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('login')

    
class ConvocatoriaUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Convocatoria
    template_name = 'Convocatorias/Gestionar_Convocatorias.html'
    fields = ['nombre_convocatoria','evento','fecha', 'hora', 'ubicacion']
    success_url = reverse_lazy('Gestionar_Convocatorias')    
    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance                                     
        # Check if a Convocatoria with the same name already exists (excluding current instance)
        existing_conv = Convocatoria.objects.filter(nombre_convocatoria=instance.nombre_convocatoria).exclude(pk=instance.pk).exists()
        if existing_conv:
            # If there's an existing convocatoria with the same name, return an error
            form.add_error('nombre_convocatoria', 'Ya existe una convocatoria con ese nombre.')
            return self.form_invalid(form)

        # Assign the event to the instance
        evento_id = form.cleaned_data.get('evento_id')
        if evento_id:
            evento = Evento.objects.get(pk=evento_id)
            instance.evento = evento
            instance.save()              
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_staff 
    
    def handle_no_permission(self):
        return redirect('login')


class ConvocatoriaDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Convocatoria
    template_name = 'Convocatorias/Gestionar_Convocatorias.html'
    success_url = reverse_lazy('Gestionar_Convocatorias')

    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')