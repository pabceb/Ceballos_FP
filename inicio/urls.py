from django.urls import path
from inicio.views import inicio, pacientes, agregar_paciente, ver_paciente, eliminar_paciente, editar_paciente,about

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('pacientes/', pacientes, name = 'pacientes'),
    path('about-me/', about, name='about'),
    path('agregar_paciente/', agregar_paciente, name = 'agregar_paciente'),
    path('pacientes/<int:id_paciente>', ver_paciente, name = 'ver_paciente'),
    path('pacientes/<int:id_paciente>/editar_paciente/', editar_paciente, name = 'editar_paciente'),
    path('pacientes/<int:id_paciente>/eliminar/', eliminar_paciente, name = 'eliminar_paciente'),

]
