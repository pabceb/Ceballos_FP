from django.urls import path
from inicio.views import inicio, pacientes, agregar_paciente

# cada app tiene que tener sus propios caminos
urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('pacientes/', pacientes, name = 'pacientes'),
    path('nuevo-paciente/', agregar_paciente, name = 'agregar_paciente'),

]
