from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.forms import CreacionDeUsuario, EdicionPerfil
from usuarios.models import DatosExtras



def login(request):
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')   
            user = authenticate(username = usuario, password = contrasenia)
            django_login(request, user)
            return redirect('inicio')
    return render(request, 'usuarios/login.html', {'formulario': formulario})
 
def registro(request):
    formulario = CreacionDeUsuario()
    if request.method == 'POST':
        formulario = CreacionDeUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def perfil(request):
    return render(request, 'usuarios/perfil.html')

def editar_perfil(request):   
    user = request.user
    datos_extra, _ = DatosExtras.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            avatar = formulario.cleaned_data.get('avatar')
            bio = formulario.cleaned_data.get('bio')
            # avatar = formulario.cleaned_data.get('datos_extra.avatar')
            # bio = formulario.cleaned_data.get('datos_extra.bio')
            if bio:
                datos_extra.bio = bio
                datos_extra.save()    
            # if avatar and datos_extra.avatar:
            # if avatar or datos_extra.avatar:
            if avatar:
                datos_extra.avatar = avatar
            datos_extra.save()
            formulario.save()
            # no entra
            return redirect('perfil')
    else:
        formulario = EdicionPerfil(initial={'avatar': datos_extra.avatar},instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class cambiarContrasenia(PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('perfil')
    