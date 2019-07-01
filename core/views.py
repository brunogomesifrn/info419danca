from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def Estilos(request)
	return render(request):


def Dancarino(request)
	return render(request):


def inscritos(request)
	return render(request, 'inscritos.html')


# Create your views here.
def inicial(request):
	return render(request, 'index.html')
@login_required
def perfil(request):
	return render(request, 'perfil.html')
def registro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
	'form': form
	}
	return render(request, 'registro.html', contexto)