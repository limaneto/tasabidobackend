# -*- coding: utf-8 -*-
from IPython.utils import generics

from django.db import IntegrityError
from django.http import HttpResponse
from django.core.mail import BadHeaderError, EmailMessage
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from tasabido.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasabido.serializers import UsuarioSerializer, DuvidaSerializer, MateriaSerializer, SubtopicoSerializer, \
    MonitoriaSerializer, MoedaSerializer
from .models import Duvida, Materia, Subtopico, Monitoria, Moeda


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
        moeda = Moeda(usuario=usuario)
        moeda.save()
        success = True
        message = 'Usuario Cadastrado Com Sucesso'
        return Response({'success': success, 'message': message, 'username': login, 'id': usuario.id})
    else:
        success = False
        message = 'Ocorreu algum problema'
        return Response({'success': success, 'message': message})


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
            message = u'Usuario Cadastrado Com Sucesso'
            return Response({'success': success, 'message': message, 'username': login, 'id': user.id,
                             'first_name': user.first_name, 'email': user.email})

        else:
            success = False
            message = u'Usuario Não Ativo'
            return Response({'success': success, 'message': message})
    else:
        success = False
        message = u'Ocorreu algum problema, tente mais tarde'
        return Response({'success': success, 'message': message})


@csrf_exempt
@api_view(['POST'])
def cadastrar_monitoria(request):
    endereco = request.data.get('endereco', '')
    titulo = request.data.get('titulo', '')
    descricao = request.data.get('descricao', '')
    data_monitoria = request.data.get('data_monitoria')
    dia_monitoria = request.data.get('dia', '')
    hora_monitoria = request.data.get('hora', '')
    id_usuario = request.data['id_usuario']
    id_materia = request.data['id_materia']
    user = User.objects.get(pk=id_usuario)
    materia = Materia.objects.get(pk=id_materia)
    monitoria = Monitoria(titulo=titulo, descricao=descricao, endereco=endereco, data_monitoria=data_monitoria,
                          dia=dia_monitoria, horario=hora_monitoria)
    ids_subtopico = request.data.get('ids_subtopicos')
    subtopicos = Subtopico.objects.filter(id__in=ids_subtopico)
    monitoria.usuario = user
    monitoria.username = user.username
    monitoria.materia = materia
    monitoria.save()
    monitoria.subtopico = subtopicos
    monitoria.save()
    monitoriaSer = MonitoriaSerializer(monitoria)
    if monitoria.pk is not None:

        message = u'Monitoria Cadastrada com Sucesso'
        return Response({'success': True, 'message': message, 'id': monitoria.pk})
    else:
        message = u'Ocorreu algum problema, tente mais tarde'
        return Response({'success': False, 'message': message})


@csrf_exempt
@api_view(['POST'])
def cadastrar_materia(request):
    nome = request.POST.get('nome', '')
    materia = Materia(nome=nome)
    materia.save()
    materiaSerialiazed = MateriaSerializer(materia)
    return Response({'success': True, 'data': {'materia': materiaSerialiazed.data}})


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
    return Response({'sucess': True, 'data': {'subtopico': subtopicoSerialiazed.data}})


@csrf_exempt
@api_view(['POST'])
def cadastrar_duvida(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '')
        descricao = request.POST.get('descricao', '')
        data_duvida = request.POST.get('data_duvida', '')
        id_usuario = request.POST['id_usuario']
        id_subtopico = request.POST['id_subtopico']
        user = User.objects.get(pk=id_usuario)
        subtopico = Subtopico.objects.get(pk=id_subtopico)
        duvida = Duvida(titulo=titulo, descricao=descricao, data_duvida=data_duvida)
        duvida.usuario = user
        duvida.username = user.username
        duvida.subtopico = subtopico
        duvida.save()
        success = True
        if duvida.pk is not None:
            message = 'Duvida Cadastrada com Sucesso'
            return Response({'success': success, 'message': message, 'id': duvida.pk})
        else:
            success = False
            message = 'Ocorreu algum problema'
            return Response({'success': success, 'message': message})


@csrf_exempt
@api_view(['POST'])
def atualizar_duvida(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '')
        data_duvida = request.POST.get('data_duvida', '')
        descricao = request.POST.get('descricao', '')
        id_usuario = request.POST['id_usuario']
        id_subtopico = request.POST['id_subtopico']
        id_duvida = request.POST.get('id_duvida', '')
        user = User.objects.get(pk=id_usuario)
        subtopico = Subtopico.objects.get(pk=id_subtopico)
        duvida = Duvida.objects.get(pk=id_duvida)

        if duvida.usuario_id == int(id_usuario):
            duvida.titulo = titulo
            duvida.descricao = descricao
            duvida.data_duvida = data_duvida
            duvida.usuario = user
            duvida.subtopico = subtopico
            duvida.save()
            return Response({'success': True, 'message': 'Duvida Atualizada com Sucesso', 'id': duvida.pk})
        else:
            return Response({'success': False, 'message': 'Ocorreu algum problema'})

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
            return Response({'success': True, 'message': message})
        else:
            message = u'Usuário não é o criador dessa dúvida'
            return Response({'success': False, 'message': message})


@csrf_exempt
@api_view(['POST'])
def deletar_monitoria(request):
    id_usuario = request.data.get('id_usuario', '')
    id_monitoria = request.data.get('id_monitoria', '')
    monitoriaToDelete = Monitoria.objects.get(pk=id_monitoria)

    if monitoriaToDelete.usuario_id == int(id_usuario):
        monitoriaToDelete.delete()
        message = u'Monitoria deletada com sucesso'
        return Response({'success': True, 'message': message})
    else:
        message = u'Usuário não é o criador dessa monitoria'
        return Response({'success': False, 'message': message})


@csrf_exempt
@api_view(['POST'])
def pagamento(request):
    id_usuario_pagante = request.data.get('id_usuario_pagante', '')
    username = request.data.get('username', '')
    quantia = request.data.get('quantia', '')

    user_pag = User.objects.get(pk=id_usuario_pagante)
    user_rec = User.objects.get(username=username)

    moeda_pag = Moeda.objects.get(usuario=user_pag)
    moeda_rec = Moeda.objects.get(usuario=user_rec)
    quantia_int = int(quantia)

    if moeda_pag.quantia >= quantia_int:
        moeda_rec.quantia += quantia_int
        moeda_pag.quantia -= quantia_int
        moeda_rec.save()
        moeda_pag.save()
        message = 'Pagamento efetuado com sucesso.'
        return Response({'success': True, 'message': message, 'moeda': moeda_pag.quantia})
    else:
        message = 'Não tem moedas suficiente.'
        return Response({'success': False, 'message': message})


@api_view(['POST'])
def send_email(request):
    id_to = request.POST.get('id_to', '')
    user_to = User.objects.get(pk=id_to)
    to_email = user_to.email

    assunto = request.POST.get('assunto', '')
    message = request.POST.get('message', '')

    if assunto and message and to_email:
        try:
            email = EmailMessage(assunto, message, to=[to_email])
            email.send()
        except BadHeaderError:
            return Response({'success': False, 'message': 'Ocorreu algum problema'})
        return Response({'success': True, 'message': 'Email Enviado'})
    else:
        return Response({'success': False, 'message': 'Preencha todos os campos'})


class UsuariosModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'username'


class MateriasModelViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer


class SubtopicosListViewSet(generics.ListAPIView):
    queryset = Subtopico.objects.all()
    serializer_class = SubtopicoSerializer

    def get_queryset(self):
        id_materia = self.kwargs['materia']
        return Subtopico.objects.filter(materia=id_materia)


class SubtopicosModelViewSet(viewsets.ModelViewSet):
    queryset = Subtopico.objects.all()
    serializer_class = SubtopicoSerializer


class DuvidaModelViewSet(viewsets.ModelViewSet):
    queryset = Duvida.objects.all()
    serializer_class = DuvidaSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class MonitoriaModelViewSet(viewsets.ModelViewSet):
    queryset = Monitoria.objects.all()
    serializer_class = MonitoriaSerializer


class MoedaListView(viewsets.ModelViewSet):
    queryset = Moeda.objects.all()
    serializer_class = MoedaSerializer
    lookup_field = 'usuario'
