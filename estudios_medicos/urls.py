from django.urls import path
from estudios_medicos import views

urlpatterns = [
    path('estudios_rx/', views.EstudiosRX.as_view(), name='estudios_rx'),
    path('estudios_rx/nuevo_estudio/', views.CrearEstudioRx.as_view(), name='crear_estudio_rx')
]
