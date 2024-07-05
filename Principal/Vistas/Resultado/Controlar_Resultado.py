from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from Principal.Modelos.Evento.Evento import Evento
from Principal.Modelos.Inscripcion.Inscripcion import Inscripcion
from Principal.Modelos.Resultado.Resultado import Resultado
from Principal.Modelos.Usuario.Usuario import Usuario


class Ver_Resultados(LoginRequiredMixin ,UserPassesTestMixin,ListView):
    model = Resultado
    template_name = 'Resultados/Ver_Resultados.html'  
    context_object_name = 'resu'
    paginate_by = 5
      
    def get_queryset(self) -> QuerySet[Any]:
        
        q = self.request.GET.get('q')
        if q:
            return Resultado.objects.filter(get_nombre_equipo__icontains=q)
        return super().get_queryset()
    
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return reverse_lazy('login')    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        return context

class Gestionar_Resultados(LoginRequiredMixin ,UserPassesTestMixin,ListView):
    model = Resultado
    template_name = 'Resultados/Gestionar_Resultados.html'  
    context_object_name = 'resu'
    paginate_by = 5
          
    def get_queryset(self) -> QuerySet[Any]:
        
        q = self.request.GET.get('q')
        if q:
            return Resultado.objects.filter(get_nombre_equipo__icontains=q)
        return super().get_queryset()
    
    def get_queryset2(self):
        return Inscripcion.objects.all()
    
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return reverse_lazy('login')    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        context['incri'] = Inscripcion.objects.all()
        return context    
    
class Agregar_Resultado(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Resultado
    template_name = 'Resultados/Gestionar_Resultados.html'
    fields = ['inscripcion','evento','puesto', 'puntuacion']
    success_url = "/Gestionar_Resultados/?created"

    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance
        # Assign the event to the instance     
        if Resultado.objects.filter(inscripcion__nombre_equipo=instance.inscripcion.nombre_equipo).exists():
            return self.form_invalid(form)
        incri_id = form.cleaned_data.get('incri_id')
        evento_id = form.cleaned_data.get('evento_id')
        print(instance)
        if incri_id and evento_id:
            inscripcion = Inscripcion.objects.get(pk=incri_id)
            evento = Evento.objects.get(pk=evento_id)
            instance.inscripcion = inscripcion
            instance.evento = evento   
            instance.save()    
        return super().form_valid(form)      
    
    def form_invalid(self, form):
        return redirect("/Gestionar_Resultados/?error")    
     
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return reverse_lazy('login')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        return context  
    
class Modificar_Resultado(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Resultado
    template_name = 'Resultados/Gestionar_Resultados.html'
    fields = ['inscripcion','evento','puesto', 'puntuacion']
    success_url = "/Gestionar_Resultados/?edit"
    
    def form_valid(self, form):
        # Get the instance being updated
        instance = form.instance
        # Assign the event to the instance         
        incri_id = form.cleaned_data.get('incri_id')
        evento_id = form.cleaned_data.get('evento_id')
        print(instance)
        if incri_id and evento_id:
            inscripcion = Inscripcion.objects.get(pk=incri_id)
            evento = Evento.objects.get(pk=evento_id)
            instance.inscripcion = inscripcion
            instance.evento = evento   
            instance.save()    
        return super().form_valid(form)          
     
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return reverse_lazy('login')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_custom'] = Usuario.objects.get(id = self.request.user.id)
        return context  
    
class Eliminar_Resultado(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Resultado
    template_name = 'Resultados/Gestionar_Resultados.html'
    success_url = "/Gestionar_Resultados/?delete"

    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        return redirect('login')    