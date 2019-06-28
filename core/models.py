from django.db import models

class Estilos(models.Model):
nome = models.CharField('nome', max_length=100)
