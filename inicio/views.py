from django.shortcuts import render, redirect
from django.http import HttpResponse

from inicio.models import Paciente
from inicio.forms import FormularioCreacionPaciente, FormularioBuscarPaciente, FormularioEdicionPaciente

def inicio(request):
    # return HttpResponse('Hola Mundo!')
    diccionario = {}
    return render(request, 'inicio/inicio.html', diccionario)
    # return render(request, 'base.html')



def pacientes(request):
    # mostrar listado de pacientes
    # pacientes = Paciente.objects.all()
    # revisar si hay que crear pacientes
    formulario_buscar = FormularioBuscarPaciente(request.GET)
    if formulario_buscar.is_valid():
        afiliado = formulario_buscar.cleaned_data.get('n_afiliado')
        pacientes = Paciente.objects.filter(n_afiliado__icontains = afiliado)
        
    return render(request, 'inicio/pacientes.html', {'pacientes': pacientes, 'formulario_buscar': formulario_buscar})

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
    return render(request, 'inicio/agregar_paciente.html', {'formulario_crear_paciente': formulario_crear_paciente})

# se modifica CRUD

def eliminar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    paciente.delete()
    return redirect('pacientes')

def editar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    formulario_editar_paciente = FormularioEdicionPaciente()
    if request.method == 'POST':
        formulario_editar_paciente = FormularioEdicionPaciente(request.POST)
        if formulario_editar_paciente.is_valid():
            info_nueva = formulario_editar_paciente.cleaned_data
            paciente.nombre = info_nueva.get('nombre')
            paciente.apellido = info_nueva.get('apellido')
            paciente.dni = info_nueva.get('dni')
            paciente.plan = info_nueva.get('plan')
            paciente.n_afiliado = info_nueva.get('n_afiliado')
            
            paciente.save()
            return redirect('pacientes')
    
    
    
    return render(request, 'inicio/editar_paciente.html', {'paciente': paciente, 'formulario': formulario_editar_paciente})

def ver_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)    
    return render(request, 'inicio/ver_paciente.html', {'paciente': paciente})