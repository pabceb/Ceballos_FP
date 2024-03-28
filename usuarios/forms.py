from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreacionDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contrasenia', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {llave: '' for llave in fields}
        


