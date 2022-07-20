from django.db import models

class Produto(models.Model):
    produto = models.CharField(verbose_name='Produto', max_length=100, unique=True)
    preco = models.DecimalField(verbose_name='Preço unitário', max_digits=7, decimal_places=2)
    estoque = models.IntegerField(verbose_name='Estoque atual')
    estoque_minimo = models.PositiveIntegerField(verbose_name='estoque mínimo', default=0)
    data_cadastro = models.DateField(verbose_name='Data do Cadastro', null=True, blank=True)
    ativo = models.BooleanField(verbose_name='Situação')

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto