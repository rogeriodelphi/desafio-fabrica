from django.db import models

class Cliente(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    email = models.EmailField(verbose_name='E-mail', blank=False, max_length=60, )
    cpf = models.CharField(verbose_name='CPF', max_length=11, unique=True)
    rg = models.CharField(verbose_name='RG', max_length=9)
    celular = models.CharField(verbose_name='Celular', max_length=14)
    ativo = models.BooleanField(verbose_name='Situação')

    def __str__(self):
        return self.nome