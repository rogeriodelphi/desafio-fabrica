from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

class Pedido(models.Model):
    STATUS = (
        ('AP', 'Aprovado'),
        ('CA', 'Cancelado'),
        ('PE', 'Pendente'),
        ('EM', 'Em Análise')
    )


    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    produto = models.ManyToManyField(Produto, verbose_name='Produto')
    status = models.CharField(verbose_name='Situação', max_length=2, choices=STATUS, blank=False, null=False, default='EM' )
    observacao = models.TextField(verbose_name='Observações', max_length=500, blank=True, null=True)
    data_pedido = models.DateTimeField(verbose_name='Data do Pedido')
    valor_total = models.DecimalField('Valor Total (R$)', max_digits=7, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.observacao