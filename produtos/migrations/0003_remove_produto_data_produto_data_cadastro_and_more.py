# Generated by Django 4.0.6 on 2022-07-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto_ativo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='data',
        ),
        migrations.AddField(
            model_name='produto',
            name='data_cadastro',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Cadastro'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='ativo',
            field=models.BooleanField(verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(verbose_name='Estoque atual'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço unitário'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='produto',
            field=models.CharField(max_length=100, unique=True, verbose_name='Produto'),
        ),
    ]
