from django.db import models
from django.views.generic.list import ListView

class Estudio(ListView):
    nombre = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 20)
    n_afiliado = models.CharField(max_length = 20)
    profesional = models.CharField(max_length = 20)
    fecha_estudio = models.DateField()
    
    def __str__(self):
        return f'Estudio: {self.nombre} {self.tipo} ({self.fecha_estudio})'