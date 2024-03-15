from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    # return HttpResponse('Hola Mundo!')
    diccionario = {}
    return render(request, 'index.html', diccionario)

def pacientes(request):
    ...
    return HttpResponse('Lista de pacientes')

def agregar_paciente(request):
    ...
    return HttpResponse('Agregar nuevo paciente')