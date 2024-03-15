from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Paciente
from inicio.forms import FormularioCreacionPaciente

def inicio(request):
    # return HttpResponse('Hola Mundo!')
    diccionario = {}
    return render(request, 'index.html', diccionario)

def pacientes(request):
    # mostrar listado de pacientes
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes': pacientes})

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
    if request.method == 'POST':
        formulario_crear_paciente = FormularioCreacionPaciente(request.POST)
        if formulario_crear_paciente.is_valid():
            nombre = formulario_crear_paciente.cleaned_data.get('nombre')
            apellido = formulario_crear_paciente.cleaned_data.get('apellido')
            dni = formulario_crear_paciente.cleaned_data.get('dni')
            plan = formulario_crear_paciente.cleaned_data.get('plan')
            paciente_n = Paciente(nombre = nombre, apellido = apellido, dni = dni, plan = plan)
            paciente_n.save()
            return redirect('pacientes')
    
    
    
    return render(request, 'agregar_paciente.html', {'formulario_crear_paciente': formulario_crear_paciente})