from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from estudios_medicos.models import Estudios_rx

# uso de Clases Basadas en Vistas

# def estudios_rx(request):
#     ...

# mixin para CBV para limitar el acceso cuando no se inicia sesión. Para Editar y Eliminar

class EstudiosRX(ListView):
    model = Estudios_rx
    template_name = "estudios_rx/estudios_rx.html"
    # se agrega
    context_object_name = 'estudios_rx'
    

class CrearEstudioRx(CreateView):
    model = Estudios_rx
    template_name = "estudios_rx/crear_estudio_rx.html"
    fields = ['nombre', 'tipo', 'n_afiliado', 'profesional', 'fecha_estudio', 'imagen']
    success_url = reverse_lazy('estudios_rx')
    
class EliminarEstudioRX(LoginRequiredMixin, DeleteView):
    model = Estudios_rx
    template_name = "estudios_rx/eliminar_estudio_rx.html"
    success_url = reverse_lazy('estudios_rx')

class EditarEstudioRX(LoginRequiredMixin, UpdateView):
    model = Estudios_rx
    template_name = "estudios_rx/editar_estudio_rx.html"
    fields = ['nombre', 'tipo', 'n_afiliado', 'profesional', 'fecha_estudio', 'imagen']
    success_url = reverse_lazy('estudios_rx')
    
class DetallesEstudioRX(DetailView):
    model = Estudios_rx
    template_name = "estudios_rx/detalles_estudio_rx.html"