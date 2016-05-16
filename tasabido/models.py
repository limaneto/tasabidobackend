from django.db import models
from django.forms import ModelForm

# Create your models here.

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __unicode__(self):
    	return self.nome_usuario
    

class Duvida(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)

    def __unicode__(self):
    	return self.titulo

class Ajuda(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)

    def __unicode__(self):
    	return self.titulo

class Materia(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
    	return self.nome