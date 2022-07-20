from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    item = models.ManyToManyField(Produto)
    quantidade = models.PositiveIntegerField()
    ativo = models.BooleanField()
    observacao = models.TextField(max_length=500, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.observacao