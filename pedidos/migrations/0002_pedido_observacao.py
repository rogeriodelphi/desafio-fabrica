# Generated by Django 4.0.6 on 2022-07-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='observacao',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
