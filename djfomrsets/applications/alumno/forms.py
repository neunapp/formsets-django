from django import forms
#
from .models import Alumno, Asistencia


class AlumnoForm(forms.ModelForm):
    
    class Meta:
        model = Alumno
        fields = (
            'full_name',
            'gender',
        )


class AsistenciaForm(forms.ModelForm):
    
    class Meta:
        model = Asistencia
        fields = (
            'alumno',
        )