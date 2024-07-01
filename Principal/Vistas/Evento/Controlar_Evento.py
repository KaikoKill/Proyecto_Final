from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Principal.Modelos.Evento.Evento import Evento
from Principal.Modelos.Usuario.Usuario import Usuario
from Principal.Vistas.Evento.forms import EventoModelForm, EventoUpdateModelForm
  
    
class Gestionar_Eventos(LoginRequiredMixin ,UserPassesTestMixin,ListView):
    model = Evento
    template_name = 'Eventos/Gestionar_Eventos.html'  
    context_object_name = 'eventos'
      
    def get_queryset(self):
        return Evento.objects.all()
    
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return reverse_lazy('login')    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        return context    
    
class EventoCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Evento
    template_name = 'Eventos/Gestionar_Eventos.html'
    form_class = EventoModelForm
    success_url = reverse_lazy('Gestionar_Eventos')
    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance
        # Check if is being set to True
        existing_event = Evento.objects.filter(nombre_evento = instance.nombre_evento ).exclude(pk=instance.pk).exists()
        if existing_event:
                # If there's an existing event, return an error
                form.add_error('nombre_evento', 'Ya existe un evento con ese nombre .')
                return self.form_invalid(form)
        # Call the parent class's form_valid method
        instance.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')
        

class EventoUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Evento
    template_name = 'Eventos/Gestionar_Eventos.html'
    form_class = EventoUpdateModelForm
    success_url = reverse_lazy('Gestionar_Eventos')    
    
    
    def form_valid(self, form):
        instance = form.instance
        instance.save()
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_staff 
    
    def handle_no_permission(self):
        return redirect('login')


class EventoDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Evento
    template_name = 'Eventos/Gestionar_Eventos.html'
    success_url = reverse_lazy('Gestionar_Eventos')

    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')