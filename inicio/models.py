from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    # id = models.IntegerField()
    plan = models.CharField(max_length = 10)
    