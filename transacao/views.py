# views.py
import json
from django.http import request,JsonResponse
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Cliente, Transacao
from .serializers import ClienteSerializer, TransacaoSerializer
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
def TransacaoView(request,id):
    if request.method == "POST":
        try:
            cliente = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
        
        request.data['cliente'] = cliente.id  # Definindo o cliente nos dados da requisição

        serializer = TransacaoSerializer(data=request.data)
        if serializer.is_valid():
            transacao = serializer.save(cliente=cliente)
            if transacao.tipo == 'c':
                cliente.saldo += transacao.valor
            else:
                cliente.saldo -= transacao.valor
                if cliente.saldo < cliente.limite:
                    cliente.saldo += transacao.valor  # Revertendo a transação
                    return JsonResponse(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            cliente.save()
            return JsonResponse({'limite': cliente.limite, 'saldo': cliente.saldo}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=400)

        
        

@api_view(['GET'])
def ExtratoView(request,id):
    if request.method == "GET":
        try:
            cliente = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND)
        
        request.data['cliente'] = cliente.id  # Definindo o cliente nos dados da requisição
        transacoes = Transacao.objects.filter(cliente=id).order_by('-realizada_em')[:10]
        saldo_total = cliente.saldo
        limite = cliente.limite

        serializer = ClienteSerializer(cliente)
        data = serializer.data
        data['saldo'] = {
            'total': saldo_total,
            'data_extrato': transacoes.first().realizada_em if transacoes else None,
            'limite': limite
        }
        data['ultimas_transacoes'] = TransacaoSerializer(transacoes, many=True).data
        return JsonResponse(data, status=status.HTTP_200_OK)
