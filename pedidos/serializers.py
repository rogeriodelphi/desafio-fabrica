from rest_framework import serializers

import clientes.models
from pedidos.models import Pedido
# from pedidos.validators import *


class PedidoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = Pedido
        fields = ('id', 'data_pedido', 'valor_total', 'cliente', 'status', 'produto')

    def get_status(self, obj):
        return obj.get_status_display()


class ListaPedidosClienteSerializer(serializers.ModelSerializer):
    cliente = serializers.ReadOnlyField(source='cliente.nome')
    status = serializers.SerializerMethodField()
    class Meta:
        model = Pedido
        fields = ['cliente', 'id', 'data_pedido', 'status', 'produto', 'valor_total',  'observacao']

    def get_status(self, obj):
        return obj.get_status_display()

class ListaPedidosProdutoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = Pedido
        fields = ['id', 'data_pedido', 'status', 'valor_total',  'observacao']

    def get_status(self, obj):
        return obj.get_status_display()