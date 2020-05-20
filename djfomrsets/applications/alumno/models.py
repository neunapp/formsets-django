from django.db import models
from django.utils import timezone


# Create your models here.
class Alumno(models.Model):

    VARON = '0'
    MUJER = '1'
    OTRO = '2'
    GENDER_CHOICES = [
        (VARON, 'Varon'),
        (MUJER, 'Mujer'),
        (OTRO, 'Otro'),
    ]

    full_name = models.CharField(
        'Nombres',
        max_length=60
    )
    gender = models.CharField(
        'Genero',
        max_length=1,
        choices=GENDER_CHOICES
    )

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        return self.full_name


class Asistencia(models.Model):

    alumno = models.ForeignKey(
        Alumno, 
        on_delete=models.CASCADE
    )
    fecha = models.DateField(default=timezone.now)
    

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        return self.alumno.full_name

    