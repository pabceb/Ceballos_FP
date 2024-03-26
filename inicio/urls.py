from django.urls import path
from inicio.views import inicio, pacientes, agregar_paciente, ver_paciente, eliminar_paciente, editar_paciente

# cada app tiene que tener sus propios caminos
urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('pacientes/', pacientes, name = 'pacientes'),
    path('agregar_paciente/', agregar_paciente, name = 'agregar_paciente'),
    path('pacientes/<int:id_paciente>', ver_paciente, name = 'ver_paciente'),
    path('pacientes/<int:id_paciente>', editar_paciente, name = 'editar_paciente'),
    path('pacientes/<int:id_paciente>/eliminar/', eliminar_paciente, name = 'eliminar_paciente'),

]
