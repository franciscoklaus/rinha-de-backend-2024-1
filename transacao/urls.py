# urls.py
from django.urls import path
from .views import TransacaoView, ExtratoView

urlpatterns = [
    path('clientes/<int:id>/transacoes', TransacaoView, name='transacoes'),
    path('clientes/<int:id>/extrato', ExtratoView, name='extrato'),
]
