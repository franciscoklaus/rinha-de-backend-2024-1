from django.db import models


class Cliente(models.Model):
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.id}"

class Transacao(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=[('c', 'Crédito'), ('d', 'Débito')])
    descricao = models.CharField(max_length=10)
    realizada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - R$ {self.valor:.2f} - {self.descricao}"