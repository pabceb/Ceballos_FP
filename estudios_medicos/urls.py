from django.urls import path
from estudios_medicos import views

urlpatterns = [
    path('estudios_rx/', views.EstudiosRX.as_view(), name='estudios_rx'),
    path('estudios_rx/nuevo_estudio_rx/', views.CrearEstudioRx.as_view(), name='crear_estudio_rx'),
    path('estudios_rx/<int:pk>/', views.DetallesEstudioRX.as_view(), name='detalles_estudio_rx'),
    path('estudios_rx/<int:pk>/editar_estudio_rx/', views.EditarEstudioRX.as_view(), name='editar_estudio_rx'),
    path('estudios_rx/<int:pk>/eliminar_estudio_rx/', views.EliminarEstudioRX.as_view(), name='eliminar_estudio_rx'),
    
    
]


