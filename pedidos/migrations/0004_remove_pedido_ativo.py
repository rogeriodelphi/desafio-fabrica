# Generated by Django 4.0.6 on 2022-07-20 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_pedido_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='ativo',
        ),
    ]
