from django.contrib import admin
from .models import Pacientes

# Register your models here.

class PacientesAdmin(admin.ModelAdmin):
    list_display = ['nombrePaciente','apellidoPaciente', 'rutPaciente', 'fechaNacimiento', 'correoPaciente']
    
admin.site.register(Pacientes, PacientesAdmin)
