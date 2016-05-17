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
from tasabido.serializers import UsuarioSerializer
from .models import Usuario, Duvida, Ajuda


# Create your views here.
def index(requests):
    return HttpResponse("Bem vindo maxo!")


@csrf_exempt
def criar_usuario(request):
    nome = request.POST['nome_usuario']
    curso = request.POST['curso']
    senha = request.POST['senha']
    # curso = Usuario(**request.POST)
    usuario = Usuario(nome_usuario=nome, curso=curso, senha=senha)
    usuario.save()
    return HttpResponse("Bem vindo maxo!")



def usuarios(request):
    usuarios = UsuarioSerializer(Usuario.objects.all(), many=True).data
    # usuarios = Usuario.objects.all()
    # return render(request, 'tasabido/detail.html', {'usuarios': usuarios})
    return Response({
        'usuarios': usuarios,
    })


@csrf_exempt
def criar_duvida(request):
    nome = request.POST['nome_usuario']
    curso = request.POST['curso']
    senha = request.POST['senha']
    # curso = Usuario(**request.POST)
    usuario = Usuario(nome_usuario=nome, curso=curso, senha=senha)
    usuario.save()
    return HttpResponse("Bem vindo maxo!")

def duvidas(request):
    duvidas = Duvida.objects.all()
    return render(request, 'tasabido/duvidas.html', {'duvidas': duvidas})


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
