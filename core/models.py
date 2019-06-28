from django.db import models

class Estilos(models.Model):
nome = models.CharField('Nome', max_length=50)
class Dancarino(models.Model):
nome = models.CharField('Nome', max_length=50)
perfil = models.ForeignKey('perfil', on_delete=models.CASCATE)
curso = models.CharField('cursos', max_length=30)
periodo = models.ForeignKey(Areas, on_delete=models.CASCATE)
idade = model.YEAR('idade',)
imagem = models.ImageField(candidatos)