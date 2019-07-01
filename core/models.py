from django.db import models

class Estilos(models.Model):
	nome = models.CharField('Nome', max_length=50)
class Dancarino(models.Model):
	nome = models.CharField('Nome', max_length=50)
	perfil = models.CharField('perfil', max_length=50)
	curso = models.CharField('cursos', max_length=30)
	idade = models.DateField('idade')
	imagem = models.ImageField(upload_to="templates")