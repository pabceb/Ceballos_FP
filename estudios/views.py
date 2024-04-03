from django.shortcuts import render
from django.views.generic.edit import CreateView
from estudios.models import Estudio
from django.urls import reverse_lazy

def Laboratorio(request):
    model = Laboratorio
    context_object_name = 'estudios'
    template_name = 'estudios/estudios.html'
    return render(request, 'estudios.html')

def CrearEstudio(request, CreateView):
    model = Estudio
    template_name = 'estudios/crear_estudio.html'
    fields = ['nombre', 'tipo', 'n_afiliado', 'profesional', 'fecha_estudio']
    success_url = reverse_lazy('estudios')
    return render(request, 'estudios.html')