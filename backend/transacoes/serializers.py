from rest_framework import serializers
from .models import Transacao


class TransacaoSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source='usuario.nome', read_only=True)
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)

    class Meta:
        model = Transacao
        fields = [
            'id', 'descricao', 'valor', 'data', 'tipo', 'status',
            'usuario', 'usuario_nome', 'categoria', 'categoria_nome',
        ]

    def validate_valor(self, valor):
        if valor <= 0:
            raise serializers.ValidationError('O valor precisa ser maior que zero.')
        return valor

    def validate(self, dados):
        categoria = dados.get('categoria')
        tipo = dados.get('tipo')
        # no PATCH, o campo que não veio continua com o valor já salvo
        if self.instance:
            categoria = categoria or self.instance.categoria
            tipo = tipo or self.instance.tipo
        if categoria.tipo != tipo:
            raise serializers.ValidationError(
                'O tipo da transação precisa ser igual ao tipo da categoria.')
        return dados
