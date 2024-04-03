from django.urls import path
from estudios import views

urlpatterns = [
    path('estudios', views.Estudio.as_view(), name='estudios'),
    
]
