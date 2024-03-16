from django.shortcuts import render, redirect
from django.http import HttpResponse

from inicio.models import Paciente
from inicio.forms import FormularioCreacionPaciente, FormularioBuscarPaciente

def inicio(request):
    # return HttpResponse('Hola Mundo!')
    diccionario = {}
    return render(request, 'index.html', diccionario)

def pacientes(request):
    # mostrar listado de pacientes
    pacientes = Paciente.objects.all()
    formulario_buscar = FormularioBuscarPaciente(request.GET)
    if formulario_buscar.is_valid():
        afiliado = formulario_buscar.cleaned_data.get('n_afiliado')
        pacientes = Paciente.objects.filter(n_afiliado__icontains = afiliado)
        
    return render(request, 'pacientes.html', {'pacientes': pacientes, 'formulario_buscar': formulario_buscar})

def agregar_paciente(request):
    # v1
    # paciente = Paciente(nombre = 'nombre1', apellido = 'ape1', dni = 12345678, plan = 'plan310')
    # paciente.save()
    # return render(request, 'agregar_paciente.html', {'paciente': paciente})
    # v2
    # if request.method == 'POST':
    #     nombre = request.POST.get('nombre')
    #     apellido = request.POST.get('apellido')
    #     dni = request.POST.get('dni')
    #     plan = request.POST.get('plan')
    #     paciente = Paciente(nombre = nombre, apellido = apellido, dni = dni, plan = plan)
    #     paciente.save()
    # return render(request, 'agregar_paciente.html', {})
    
    # v3
    formulario_crear_paciente = FormularioCreacionPaciente(request.POST)
    if request.method == 'POST':
        if formulario_crear_paciente.is_valid():
            nombre = formulario_crear_paciente.cleaned_data.get('nombre')
            apellido = formulario_crear_paciente.cleaned_data.get('apellido')
            dni = formulario_crear_paciente.cleaned_data.get('dni')
            plan = formulario_crear_paciente.cleaned_data.get('plan')
            n_afiliado = formulario_crear_paciente.cleaned_data.get('n_afiliado')
            paciente_n = Paciente(nombre = nombre, apellido = apellido, dni = dni, plan = plan, n_afiliado = n_afiliado)
            paciente_n.save()
            return redirect('pacientes')    
    return render(request, 'agregar_paciente.html', {'formulario_crear_paciente': formulario_crear_paciente})
