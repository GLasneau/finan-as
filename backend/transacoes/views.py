from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Transacao
from .serializers import TransacaoSerializer


class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

    def get_queryset(self):
        transacoes = Transacao.objects.all()
        tipo = self.request.query_params.get('tipo')
        if tipo:
            transacoes = transacoes.filter(tipo=tipo.upper())
        return transacoes

    @action(detail=False, methods=['get'])
    def pendentes(self, request):
        transacoes = Transacao.objects.filter(status='PENDENTE')
        serializer = self.get_serializer(transacoes, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pagas(self, request):
        transacoes = Transacao.objects.filter(status='PAGO')
        serializer = self.get_serializer(transacoes, many=True)
        return Response(serializer.data)
