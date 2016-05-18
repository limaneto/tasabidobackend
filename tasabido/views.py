from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.core import serializers
from rest_framework.response import Response
from tasabido.serializers import UsuarioSerializer, DuvidaSerializer, AjudaSerializer, MateriaSerializer
from .models import Usuario, Duvida, Ajuda, Materia, Subtopico

# Create your views here.
def index(requests):
    return HttpResponse("Bem vindo maxo!")


@csrf_exempt
def cadastrar_usuario(request):
    nome = request.POST['nome_usuario']
    email = request.POST['email']
    senha = request.POST['senha']
    usuario = Usuario(nome_usuario=nome, email=email, senha=senha)
    usuario.save()
    return HttpResponse("Usuario cadastrado.")

@csrf_exempt
def cadastrar_duvida(request):
    titulo = request.POST['titulo']
    descricao = request.POST['descricao']
    id_usuario = request.POST['id']
    user = Usuario.objects.get(pk=id_usuario)
    duvida = Duvida(titulo=titulo, descricao=descricao)
    duvida.usuario = user
    duvida.save()
    return HttpResponse("Duvida cadastrada.")

@csrf_exempt
def cadastrar_ajuda(request):
    titulo = request.POST['titulo']
    descricao = request.POST['descricao']
    id_usuario = request.POST['id']
    user = Usuario.objects.filter(pk=id_usuario)
    ajuda = Ajuda(titulo=titulo, descricao=descricao)
    ajuda.usuario = user
    ajuda.save()
    return HttpResponse("Ajuda cadastrada.")

@csrf_exempt
def cadastrar_materia(request):
    nome = request.POST['nome']
    materia = Materia(nome=nome)
    materia.save()
    return HttpResponse("Materia cadastrada.")

@csrf_exempt
def cadastrar_subtopico(request):
    nome = request.POST['nome']
    id_materia = request.POST['id']
    materia = Materia.objects.filter(pk=id_materia)
    subtopico = Subtopico(nome=nome)
    subtopico.materia = materia
    subtopico.save()
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

class SubtopicosList(generics.ListCreateAPIView):
    queryset = Subtopico.objects.all()
    serializer_class = MateriaSerializer



# @csrf_exempt
# def buscar_duvidas_por_id_usuario(request):
#     id_usuario = request.GET('id_usuario')
#     lista_duvidas = Duvida.objects.get(pk=id_usuario)
#     # lista_duvidas = DuvidaSerializer(Duvida.objects.get(pk=id_usuario)).data
#     # serializer_class = DuvidaSerializer
#     data = serializers.serialize('json', lista_duvidas)
#     return HttpResponse(data, content_type='application/json')


# usuarios = UsuarioSerializer(Usuario.objects.all(), many=True).data
# 	# usuarios = Usuario.objects.all()
# 	# return render(request, 'tasabido/detail.html', {'usuarios': usuarios})
# 	return Response({
#         'usuarios': usuarios,
#     })
