from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'), 
    # se utiliza una vista predefinida de django
    # con esto no hace falta generar un logout en views.py
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/contrasenia/', views.cambiarContrasenia.as_view(), name='cambiar_contrasenia'),
]
