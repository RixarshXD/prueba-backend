from django import forms
from .models import Pacientes


class FormPacientes(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'

def clean_email(self):
    inputEmail = self.cleaned_data['email']
    if inputEmail.find('@') == -1:
        raise forms.ValidationError('El correo debe tener una @')
    return inputEmail