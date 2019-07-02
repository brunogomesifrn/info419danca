from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Estilos, Dancarinos
from .forms import EstilosForm, DancarinosForms


# Create your views here.
def inicial(request):
	dancarinos = Dancarinos.objects.all()
	contexto = {
	'dancarino': dancarinos
	}
	return render(request, 'index.html', contexto)

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

def estilos(request):
	lista = Estilos.objects.all()
	contexto = {
	'lista': lista
	}
	return render(request, 'estilos.html', contexto)
def cadastrar_estilo(request):
	form = EstilosForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('estilos')
	contexto = {
	'form': form
	}
	return render(request, 'cadastrar_estilo.html', contexto)
def editar_estilo(request, id):
	estilo = Estilos.objects.get(pk=id)
	form = EstilosForm(request.POST or None, instance=estilo)
	if form.is_valid():
		form.save()
		return redirect('estilos')
	contexto = {
	'form': form
	}
	return render(request, 'cadastrar_estilo.html', contexto)
def excluir_estilo(request, id):
	estilo = Estilos.objects.get(pk=id)
	estilo.delete()
	return redirect('estilos')

def dancarinos(request):
	dancarinos = Dancarinos.objects.all()
	contexto = {
	'dancarino': dancarinos
	}
	return render(request, 'dancarinos.html', contexto)
def dancarino(request):
	form = DancarinosForms(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('dancarinos')
	contexto = {
	'form': form
	}
	return render(request, 'dancarino.html', contexto)
def editardancarino(request, id):
	dancarino = Dancarinos.objects.get(pk=id)
	form = DancarinosForms(request.POST or None, request.FILES or None, instance=dancarino)
	if form.is_valid():
		form.save()
		return redirect('dancarinos')
	contexto = {
	'form': form
	}
	return render(request, 'dancarino.html', contexto)
def excluirdancarino(request, id):
	dancarino = Dancarinos.objects.get(pk=id)
	dancarino.delete()
	return redirect('dancarinos')