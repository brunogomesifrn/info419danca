class EstilosForm(ModelForm):
class Meta():
model = EstilosForm
fields = ['nome',]
widgets = {
'nome' : forms.CheckboxSelectMultiple(),	
}



class Cursos(ModelForm):
class Meta():
model
fields = ['nome', 'curso', 'idade', 'perfil', 'periodo']
widgets = {
'area' : forms.RadioSelect(),(),
'periodo' : forms.RadioSelect(),(),
'curso' : forms.RadioSelect(),(),	
}