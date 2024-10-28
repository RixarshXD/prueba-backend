from django.db import models

# Create your models here.

class Pacientes(models.Model):
    nombrePaciente =models.CharField(max_length=50)
    apellidoPaciente = models.CharField(max_length=50)
    rutPaciente = models.IntegerField()
    fechaNacimiento = models.DateField()
    correoPaciente =models.EmailField()