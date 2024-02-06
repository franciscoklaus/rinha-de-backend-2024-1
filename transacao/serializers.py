# serializers.py
from rest_framework import serializers
from .models import Cliente, Transacao

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    transacoes = TransacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = ['limite', 'saldo', 'transacoes']
