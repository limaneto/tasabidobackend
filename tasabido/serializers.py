from rest_framework import serializers
from tasabido.models import Usuario, Duvida, Ajuda

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'