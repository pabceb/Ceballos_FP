from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from estudios_medicos.models import Estudios_rx
from django.urls import reverse_lazy

# uso de Clases Basadas en Vistas

# def estudios_rx(request):
#     ...

class EstudiosRX(ListView):
    model = Estudios_rx
    template_name = "estudios_rx/estudios_rx.html"
    # se agrega
    context_object_name = 'estudios_rx'
    

class CrearEstudioRx(CreateView):
    model = Estudios_rx
    template_name = "estudios_rx/crear_estudio_rx.html"
    fields = ['nombre', 'tipo', 'n_afiliado', 'profesional', 'fecha_estudio']
    success_url = reverse_lazy('estudios_rx')