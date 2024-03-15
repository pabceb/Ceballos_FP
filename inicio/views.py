from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Paciente

def inicio(request):
    # return HttpResponse('Hola Mundo!')
    diccionario = {}
    return render(request, 'index.html', diccionario)

def pacientes(request):
    # mostrar listado de pacientes
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes': pacientes})

def agregar_paciente(request):
    # paciente = Paciente(nombre = 'nombre1', apellido = 'ape1', dni = 12345678, plan = 'plan310')
    # paciente.save()
    # return render(request, 'agregar_paciente.html', {'paciente': paciente})
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        plan = request.POST.get('plan')
        paciente = Paciente(nombre = nombre, apellido = apellido, dni = dni, plan = plan)
        paciente.save()
    
    
    
    
    return render(request, 'agregar_paciente.html', {})