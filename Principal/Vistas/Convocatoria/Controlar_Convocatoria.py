from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
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
    paginate_by = 5
      
    def get_queryset(self) -> QuerySet[Any]:
        
        q = self.request.GET.get('q')
        if q:
            return Convocatoria.objects.filter(nombre_convocatoria__icontains=q)
        return super().get_queryset()
    
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
    paginate_by = 5
      
    def get_queryset(self) -> QuerySet[Any]:
        
        q = self.request.GET.get('q')
        if q:
            return Convocatoria.objects.filter(nombre_convocatoria__icontains=q)
        return super().get_queryset()
    
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
    success_url = "/Gestionar_Convocatorias/?created"
    
    
    def form_valid(self, form):
        instance = form.instance                                     
        # Assign the event to the instance
        if Convocatoria.objects.filter(evento=form.cleaned_data['evento']).exists():
            return self.form_invalid(form)
        
        evento_id = form.cleaned_data.get('evento_id')
        if evento_id:
            evento = Evento.objects.get(pk=evento_id)
            instance.evento = evento
            instance.save()              
        return super().form_valid(form)
        
    def form_invalid(self, form):
        return redirect("/Gestionar_Convocatorias/?error")

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('login')

    
class ConvocatoriaUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Convocatoria
    template_name = 'Convocatorias/Gestionar_Convocatorias.html'
    fields = ['nombre_convocatoria','evento','fecha', 'hora', 'ubicacion']
    success_url = "/Gestionar_Convocatorias/?edit"    
    
    def form_valid(self, form):
        
        instance = form.instance                                     
        # Assign the event to the instance
        if Convocatoria.objects.filter(evento=form.cleaned_data['evento']).exists():
            return self.form_invalid(form)
        evento_id = form.cleaned_data.get('evento_id')
        if evento_id:
            evento = Evento.objects.get(pk=evento_id)
            instance.evento = evento
            instance.save()              
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return redirect("/Gestionar_Convocatorias/?error")
    
    def test_func(self):
        return self.request.user.is_staff 
    
    def handle_no_permission(self):
        return redirect('login')


class ConvocatoriaDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Convocatoria
    template_name = 'Convocatorias/Gestionar_Convocatorias.html'
    success_url = "/Gestionar_Convocatorias/?delete"

    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('login')