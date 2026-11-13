from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'senha', 'data_cadastro']
        extra_kwargs = {
            'senha': {'write_only': True},
        }

    def validate_senha(self, senha):
        return make_password(senha)
