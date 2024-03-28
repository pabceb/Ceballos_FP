from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'), 
    # se utiliza una vista predefinida de django
    # con esto no hace falta generar un logout en views.py
    path('registro/', views.registro, name='registro'),
    
]
