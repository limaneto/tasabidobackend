from django.db import models
from django.contrib.auth.models import User


class Commom(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Materia(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.nome


class Subtopico(models.Model):
    nome = models.CharField(max_length=100)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nome


class Duvida(Commom):
    data_criacao = models.DateTimeField(auto_now=True)
    data_monitoria = models.DateTimeField('Data da monitoria', blank=True, null=True)
    segunda_data_monitoria = models.DateTimeField('Data da monitoria 2', blank=True, null=True)
    terceira_data_monitoria = models.DateTimeField('Data da monitoria 3', blank=True, null=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    subtopico = models.ForeignKey(Subtopico, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.titulo


class Monitoria(Commom):
    data_monitoria = models.DateTimeField('Data da monitoria', blank=True, null=True)
    segunda_data_monitoria = models.DateTimeField('Data da monitoria 2', blank=True, null=True)
    terceira_data_monitoria = models.DateTimeField('Data da monitoria 3', blank=True, null=True)
    endereco = models.CharField(null=True, max_length=200)
    lat = models.DecimalField(decimal_places=6, max_digits=9)
    long = models.DecimalField(decimal_places=6, max_digits=9)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    subtopico = models.ManyToManyField(Subtopico)

    def __unicode__(self):
        return self.descricao