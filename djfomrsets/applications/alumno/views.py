from django.shortcuts import render
#
from django.forms import formset_factory, modelformset_factory
from django.views.generic.edit import FormView
#
from .forms import AlumnoForm, AsistenciaForm
from .models import Asistencia


class AddAlumno(FormView):
    template_name = 'alumno/add.html'
    form_class = formset_factory(AlumnoForm, extra=3)
    success_url = '.'

    def form_valid(self, form): 

        for f in form:
            print(f.cleaned_data['full_name'])
            f.save()

        return super(AddAlumno, self).form_valid(form)



class AddAsistencia(FormView):
    """ 
        Esta parte del codigo es utilizando model formsets
        No es una de mis favoritas para el tema, prefiero formset normal
        ya que el model formset no deja configurar muchas cosas,
        pero ayuda a que se haga un guardado mas directo
    """

    template_name = 'alumno/asistencia.html'
    form_class = modelformset_factory(Asistencia, form=AsistenciaForm)
    success_url = '/'

    def form_valid(self, form):
        # cuando se trabaja con model formset no es necesario hacer la iteracion
        # este puede guardar de golpe todo el conjunto de formularios
        #
        form.save() 
        return super(AddAsistencia, self).form_valid(form)