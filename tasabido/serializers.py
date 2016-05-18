from rest_framework import serializers
from tasabido.models import Usuario, Duvida, Ajuda, Subtopico, Materia

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class DuvidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duvida
        fields = '__all__'


class AjudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ajuda
        fields = '__all__'


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'

class SubtopicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopico
        fields = '__all__'