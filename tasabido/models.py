from django.db import models


# Create your models here.


class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome_usuario


class Commom(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Duvida(Commom):
    def __unicode__(self):
        return self.titulo


class Ajuda(Commom):
    def __unicode__(self):
        return self.titulo


class Materia(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome


# materia = models.ForeignKey('Materia', on_delete=models.CASCADE)