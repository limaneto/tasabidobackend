# -*- coding: utf-8 -*-

from django.db import IntegrityError
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
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
        message = u'Usuario Cadastrado Com Sucesso'
        return Response({'success': success, 'message': message, 'username': login, 'id': usuario.id})
    else:
        success = False
        message = u'Ocorreu algum problema'
        return Response({'success': success, 'message': message})



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
            message = u'Duvida Cadastrada com Sucesso'
            return Response({'success': success, 'message':message, 'id_duvida':duvida.pk})
        else:
            success = False
            message = u'Ocorreu algum problema'
            return Response({'success': success, 'message':message})

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

        message = u'Monitoria Cadastrada com Sucesso'
        return Response({'sucesso': True, 'message':message, 'id_monitoria':monitoria.pk})
    else:
        message = u'Ocorreu algum problema, tente mais tarde'
        return Response({'sucesso': False, 'message':message})


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
            message = u'Usuario Autenticado Com Sucesso'
            return Response({'success': success, 'message':message, 'username': login, 'id': user.id})

        else:
            success = False
            message = u'Usuario Não Ativo'
            return Response({'success': success, 'message':message})
    else:
        success = False
        message = u'Ocorreu algum problema, tente mais tarde'
        return Response({'success': success, 'message':message})

@csrf_exempt
@api_view(['POST'])
def atualizar_duvida(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '')
        descricao = request.POST.get('descricao', '')
        id_usuario = request.POST['id_usuario']
        id_materia = request.POST['id_materia']
        id_subtopico = request.POST['id_subtopico']
        id_duvida = request.POST['id_duvida']
        user = User.objects.get(pk=id_usuario)
        materia = Materia.objects.get(pk=id_materia)
        subtopico = Subtopico.objects.get(pk=id_subtopico)
        duvidaToDelete = Duvida.objects.get(pk=id_duvida)

        if duvidaToDelete.usuario_id == int(id_usuario):
            duvidaToDelete.delete()
        else:
            message = u'Usuário não é o criador dessa dúvida'
            return Response({'success': False, 'message':message})

        duvida = Duvida(titulo=titulo, descricao=descricao)
        duvida.usuario = user
        duvida.materia = materia
        duvida.subtopico = subtopico
        duvida.save()
        if duvida.pk is not None:
            success = True
            message = u'Duvida Atualizada com Sucesso'
            return Response({'success': success, 'message':message, 'id_duvida':duvida.pk})
        else:
            success = False
            message = u'Ocorreu algum problema'
            return Response({'success': success, 'message':message})

@csrf_exempt
@api_view(['POST'])
def deletar_duvida(request):
    if request.method == 'POST':
        id_usuario = request.POST['id_usuario']
        id_duvida = request.POST['id_duvida']
        duvidaToDelete = Duvida.objects.get(pk=id_duvida)

        if duvidaToDelete.usuario_id == int(id_usuario):
            duvidaToDelete.delete()
            message = u'Dúvida deletada com sucesso'
            return Response({'success': True, 'message':message})
        else:
            message = u'Usuário não é o criador dessa dúvida'
            return Response({'success': False, 'message':message})


@csrf_exempt
@api_view(['POST'])
def deletar_monitoria(request):
    id_usuario = request.data.get('id_usuario', '')
    id_monitoria = request.data.get('id_monitoria', '')
    monitoriaToDelete = Monitoria.objects.get(pk=id_monitoria)

    if monitoriaToDelete.usuario_id == int(id_usuario):
        monitoriaToDelete.delete()
        message = u'Monitoria deletada com sucesso'
        return Response({'success': True, 'message':message})
    else:
        message = u'Usuário não é o criador dessa monitoria'
        return Response({'success': False, 'message':message})


@csrf_exempt
@api_view(['POST'])
def atualizar_monitoria(request):
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
    id_monitoria = request.data['id_monitoria']
    user = User.objects.get(pk=id_usuario)
    materia = Materia.objects.get(pk=id_materia)
    monitoriaToDelete = Monitoria.objects.get(pk=id_monitoria)

    if monitoriaToDelete.usuario_id == int(id_usuario):
         monitoriaToDelete.delete()
    else:
        message = u'Usuário não é o criador dessa dúvida'
        return Response({'success': False, 'message':message})

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
        message = u'Monitoria Atualizada com Sucesso'
        return Response({'sucesso': True, 'message':message, 'id_monitoria':monitoria.pk})
    else:
        message = u'Ocorreu algum problema, tente mais tarde'
        return Response({'sucesso': False, 'message':message})



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

class MonitoriaManagerViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Monitoria.objects.all()
    serializer_class = MonitoriaSerializer