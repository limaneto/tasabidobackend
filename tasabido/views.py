from django.http import Http404
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from tasabido.serializers import UsuarioSerializer, DuvidaSerializer, AjudaSerializer, MateriaSerializer
from .models import Usuario, Duvida, Ajuda, Materia


# Create your views here.
def index(requests):
    return HttpResponse("Bem vindo maxo!")


@csrf_exempt
def cadastrar_usuario(request):
    nome = request.POST['nome_usuario']
    curso = request.POST['curso']
    senha = request.POST['senha']
    usuario = Usuario(nome_usuario=nome, curso=curso, senha=senha)
    usuario.save()
    return HttpResponse("Usuario cadastrado.")

@csrf_exempt
def cadastrar_duvida(request):
    titulo = request.POST['titulo']
    descricao = request.POST['descricao']
    tema = request.POST['tema']
    usuario = Duvida(titulo=titulo, descricao=descricao, tema=tema)
    usuario.save()
    return HttpResponse("Duvida cadastrada.")

@csrf_exempt
def cadastrar_ajuda(request):
    titulo = request.POST['titulo']
    descricao = request.POST['descricao']
    tema = request.POST['tema']
    ajuda = Ajuda(titulo=titulo, descricao=descricao, tema=tema)
    ajuda.save()
    return HttpResponse("Ajuda cadastrada.")

@csrf_exempt
def cadastrar_ajuda(request):
    titulo = request.POST['titulo']
    descricao = request.POST['descricao']
    tema = request.POST['tema']
    ajuda = Ajuda(titulo=titulo, descricao=descricao, tema=tema)
    ajuda.save()
    return HttpResponse("Ajuda cadastrada.")


@csrf_exempt
def cadastrar_materia(request):
    nome = request.POST['nome']
    materia = Materia(nome=nome)
    materia.save()
    return HttpResponse("Materia cadastrada.")


class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class DuvidasList(generics.ListCreateAPIView):
    queryset = Duvida.objects.all()
    serializer_class = DuvidaSerializer

class AjudasList(generics.ListCreateAPIView):
    queryset = Ajuda.objects.all()
    serializer_class = AjudaSerializer

class MateriasList(generics.ListCreateAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer