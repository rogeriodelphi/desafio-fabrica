# Generated by Django 4.0.6 on 2022-07-20 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_remove_pedido_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(default='2022-07-20'),
            preserve_default=False,
        ),
    ]