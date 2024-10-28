from django.shortcuts import render
from .models import Pacientes
from .forms import FormPacientes

# Create your views here.

def index(request):
    return render('index.html')

def listadoPacientes(request):
    pacientes = Pacientes.objects.all()
    data = {'pacientes': pacientes}
    return render(request,'listadoPacientes.html',data)

def agregarPacientes(request):
    form = FormPacientes()
    if request.method == 'POST':
        form = FormPacientes(request.POST)
        if form.is_valid():
            form.save()
            return listadoPacientes(request)
    data = {'form': form}
    return render(request,'agregarPacientes.html',data)
