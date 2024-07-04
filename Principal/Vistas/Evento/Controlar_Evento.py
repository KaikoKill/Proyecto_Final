from typing import Any
from django.db.models import QuerySet
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
    paginate_by = 5
      
    def get_queryset(self) -> QuerySet[Any]:
        
        q = self.request.GET.get('q')
        if q:
            return Evento.objects.filter(nombre_evento__icontains=q)
        return super().get_queryset()
    
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
    success_url = "/Gestionar_Eventos/?created"

    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')
        

class EventoUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Evento
    template_name = 'Eventos/Gestionar_Eventos.html'
    form_class = EventoUpdateModelForm
    success_url = "/Gestionar_Eventos/?edit"    
    
    
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
    success_url = "/Gestionar_Eventos/?delete"

    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')