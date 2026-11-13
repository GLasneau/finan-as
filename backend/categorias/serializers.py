from rest_framework import serializers
from .models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'tipo']

    def validate_nome(self, nome):
        if len(nome) < 3:
            raise serializers.ValidationError('O nome precisa ter pelo menos 3 letras.')
        return nome
