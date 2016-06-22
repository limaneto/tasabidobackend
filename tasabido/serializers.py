from rest_framework import serializers
from tasabido.models import Duvida, Subtopico, Materia, User, Monitoria, Moeda


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'


class SubtopicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopico
        fields = '__all__'


class DuvidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duvida
        fields = '__all__'


class MonitoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoria
        fields = '__all__'


class MoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moeda
        fields = '__all__'
