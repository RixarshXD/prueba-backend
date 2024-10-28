from django.shortcuts import render, redirect
from .models import Pacientes
from .forms import FormPacientes,clean_email

# Create your views here.

def index(request):
    return render(request,'index.html')

def listadoPacientes(request):
    pacientes = Pacientes.objects.all()
    data = {'pacientes': pacientes}
    return render(request,'listadoPacientes.html',data)

def registroPacientes(request):
    form = FormPacientes()
    if request.method == 'POST':
        form = FormPacientes(request.POST)
        if form.is_valid():
            form.save()
            return listadoPacientes(request)
    data = {'form': form}
    return render(request,'registroPacientes.html',data)


def eliminarPacientes(request,id):
    pacientes = Pacientes.objects.get(id = id)
    pacientes.delete()
    return redirect('/listadoPacientes')


def actualizarPacientes(request,id):
    pacientes = Pacientes.objects.get(id=id)
    form = FormPacientes(instance=pacientes)
    if request.method == 'POST':
        form = FormPacientes(request.POST, instance=pacientes)
        if form.is_valid():
            print('email', clean_email)
            form.save()
            return listadoPacientes(request)
    data = {'form': form}
    return render(request,'registroPacientes.html',data)