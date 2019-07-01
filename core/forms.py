from django.forms import ModelForm
from .models import Estilos, Dancarinos

class EstilosForm(ModelForm):
	class Meta:
		model = Estilos
		fields = ['nome']

class DancarinosForms(ModelForm):
	class Meta:
		model = Dancarinos
		fields = ['nome', 'biografia', 'curso', 'idade', 'foto', 'estilo']
#class Cursos(ModelForm):
#class Meta():
#model
#fields = ['nome', 'curso', 'idade', 'perfil', 'periodo']
#widgets = {
#'area' : forms.RadioSelect(),(),
#'periodo' : forms.RadioSelect(),(),
#'curso' : forms.RadioSelect(),(),	
#}