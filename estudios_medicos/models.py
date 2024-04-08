from django.db import models

class Estudios_rx(models.Model):
    nombre = models.CharField(max_length = 10)
    # RX, NMR, CT
    tipo = models.CharField(max_length = 20)
    # ubicacion 
    n_afiliado = models.CharField(max_length = 20)
    # linkear en DB - a futuro
    profesional = models.CharField(max_length = 20)
    # medico solicitante
    fecha_estudio = models.DateField()
    
    def __str__(self):
        return f'Estudio de paciente {self.n_afiliado}: {self.nombre} {self.tipo} ({self.fecha_estudio})'
    
    
    # NOTA: hay que agregar imagen