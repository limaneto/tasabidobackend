from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Usuario(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # nome_usuario = models.CharField(max_length=100)
#     # login = models.CharField(max_length=100)
#     # email = models.CharField(max_length=100)
#     # senha = models.CharField(max_length=100)
#
#     def __unicode__(self):
#         return self.nome_usuario


class Commom(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

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

class Subtopico(models.Model):
    nome = models.CharField(max_length=100)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nome_subtopico


# materia = models.ForeignKey('Materia', on_delete=models.CASCADE)