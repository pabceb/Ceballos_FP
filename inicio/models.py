from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    dni = models.IntegerField()
    n_afiliado = models.CharField(max_length = 20)
    plan = models.CharField(max_length = 10)
    
    
    def __str__(self):
        return f'Paciente: {self.nombre} {self.apellido} ({self.dni}) | Plan: {self.plan} - {self.n_afiliado}'