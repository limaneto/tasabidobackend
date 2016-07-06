# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Commom(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Materia(models.Model):
    nome = models.CharField("Materia", max_length=100, unique=True)

    def __unicode__(self):
        return self.nome


class Subtopico(models.Model):
    nome = models.CharField("Subtopico", max_length=100)
    materia = models.ForeignKey("Materia", related_name="subtopicos",on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nome


class Duvida(Commom):
    data_duvida = models.TextField()
    username = models.CharField(max_length=100);
    subtopico = models.ForeignKey(Subtopico, related_name="duvidas", on_delete=models.CASCADE)

    def __unicode__(self):
        return self.titulo


class Monitoria(Commom):
    data_monitoria = models.DateTimeField('Data da monitoria', blank=True, null=True)
    dia = models.CharField(max_length=100);
    horario = models.CharField(max_length=100);
    username = models.CharField(max_length=100);
    endereco = models.CharField(null=True, max_length=200)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    subtopico = models.ManyToManyField(Subtopico, related_name="monitorias")

    def __unicode__(self):
        return self.descricao


class Moeda(models.Model):
    usuario = models.ForeignKey(User, related_name="moedas", on_delete=models.CASCADE)
    quantia = models.IntegerField(default=10)

    def __unicode__(self):
        return self.usuario.username