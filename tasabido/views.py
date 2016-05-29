from django.db import IntegrityError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from tasabido.serializers import UsuarioSerializer, DuvidaSerializer, MateriaSerializer, SubtopicoSerializer, MonitoriaSerializer
from .models import Duvida, Materia, Subtopico, Monitoria


# Create your views here.
def index(requests):
    return HttpResponse("Bem vindo maxo!")


@csrf_exempt
@api_view(['POST'])
def cadastrar_usuario(request):
    nome = request.POST.get('first_name', '')
    login = request.POST.get('username', '')
    email = request.POST.get('email', '')
    senha = request.POST.get('password', '')
    try:
        usuario = User.objects.create_user(first_name=nome, username=login, email=email, password=senha)
    except IntegrityError as e:
        if 'UNIQUE constraint failed' in e.message:
            success = False
            message = 'Login em uso'
            return Response({'success': success, 'message': message})

    usuario.save()
    if usuario.pk is not None:
        success = True
        return Response({'success': success, 'username': login, 'id': usuario.id})
    else:
        success = False
        return Response({'success': success})



@csrf_exempt
@api_view(['POST'])
def cadastrar_duvida(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '')
        descricao = request.POST.get('descricao', '')
        id_usuario = request.POST['id_usuario']
        id_materia = request.POST['id_materia']
        id_subtopico = request.POST['id_subtopico']
        user = User.objects.get(pk=id_usuario)
        materia = Materia.objects.get(pk=id_materia)
        subtopico = Subtopico.objects.get(pk=id_subtopico)
        duvida = Duvida(titulo=titulo, descricao=descricao)
        duvida.usuario = user
        duvida.materia = materia
        duvida.subtopico = subtopico
        duvida.save()
        success = True
        if duvida.pk is not None:
            return Response({'success': success, 'id_duvida':duvida.pk})
        else:
            success = False
            return Response({'success': success})

@csrf_exempt
@api_view(['POST'])
def cadastrar_materia(request):
    nome = request.POST.get('nome', '')
    materia = Materia(nome=nome)
    materia.save()
    materiaSerialiazed = MateriaSerializer(materia)
    return Response({'sucesso': True, 'data': {'materia': materiaSerialiazed.data}})


@csrf_exempt
@api_view(['POST'])
def cadastrar_subtopico(request):
    nome = request.POST.get('nome')
    id_materia = request.POST['id_materia']
    materia = Materia.objects.get(pk=id_materia)
    subtopico = Subtopico(nome=nome)
    subtopico.materia = materia
    subtopico.save()
    subtopicoSerialiazed = SubtopicoSerializer(subtopico)
    return Response({'sucesso': True, 'data': {'subtopico': subtopicoSerialiazed.data}})


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def cadastrar_monitoria(request):
    endereco = request.data.get('endereco', '')
    titulo = request.data.get('titulo', '')
    descricao = request.data.get('descricao', '')
    lat = request.data.get('lat', '')
    long = request.data.get('long', '')
    data_monitoria = request.data.get('data_monitoria')
    segunda_data_monitoria = request.data.get('segunda_data_monitoria')
    terceira_data_monitoria = request.data.get('terca_data_monitoria')
    id_usuario = request.data['id_usuario']
    id_materia = request.data['id_materia']
    user = User.objects.get(pk=id_usuario)
    materia = Materia.objects.get(pk=id_materia)
    monitoria = Monitoria(titulo=titulo, descricao=descricao, endereco=endereco, data_monitoria=data_monitoria, segunda_data_monitoria=segunda_data_monitoria,
                  terceira_data_monitoria=terceira_data_monitoria, lat=lat, long=long)
    ids_subtopico = request.data.get('ids_subtopicos')
    subtopicos = Subtopico.objects.filter(id__in=ids_subtopico)
    monitoria.usuario = user
    monitoria.materia = materia
    monitoria.save()
    monitoria.subtopico = subtopicos
    monitoria.save()
    monitoriaSer = MonitoriaSerializer(monitoria)
    if monitoria.pk is not None:
        return Response({'sucesso': True, 'data': {'monitoria': monitoriaSer.data}})
    else:
        return Response({'sucesso': False})


@csrf_exempt
@api_view(['POST'])
def autenticar_usuario(request):
    login = request.POST.get('username')
    senha = request.POST.get('password')
    user = authenticate(username=login, password=senha)

    if user is not None:
        # the password verified for the user
        if user.is_active:
            success = True
            return Response({'success': success, 'username': login, 'id': user.id})

        else:
            success = False
            return Response({'success': success})
    else:
        success = False
        return Response({'success': success})



class UsuariosList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer


class MateriasList(generics.ListCreateAPIView):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer


class SubtopicosList(generics.ListCreateAPIView):
    queryset = Subtopico.objects.all()
    serializer_class = SubtopicoSerializer


class DuvidasList(generics.ListCreateAPIView):
    queryset = Duvida.objects.all()
    serializer_class = DuvidaSerializer


class MonitoriasList(generics.ListCreateAPIView):
    queryset = Monitoria.objects.all()
    serializer_class = MonitoriaSerializer
