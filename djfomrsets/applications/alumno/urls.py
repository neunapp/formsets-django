from django.contrib import admin
from django.urls import path

from . import views

app_name = "alumno_app"

urlpatterns = [
    path(
        '',
        views.AddAlumno.as_view(),
        name='alumno-add'
    ),
    path(
        'asistencia/',
        views.AddAsistencia.as_view(),
        name='asistencia-add'
    ),
]