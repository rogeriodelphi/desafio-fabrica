from rest_framework import serializers

import clientes.models
from pedidos.models import Pedido
# from pedidos.validators import *


class PedidoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = Pedido
        fields = '__all__'

    def get_status(self, obj):
        return obj.get_status_display()


class ListaPedidosClienteSerializer(serializers.ModelSerializer):
    cliente = serializers.ReadOnlyField(source='cliente.nome')
    status = serializers.SerializerMethodField()
    class Meta:
        model = Pedido
        fields = ['cliente', 'produto', 'valor_total', 'status', 'observacao', 'data_pedido']

    def get_status(self, obj):
        return obj.get_status_display()

class ListaPedidosProdutoSerializer(serializers.ModelSerializer):
    produto_nome = serializers.ReadOnlyField(source='produto.produto')
    status = serializers.SerializerMethodField()
    class Meta:
        model = Pedido
        fields = ['id', 'data_pedido', 'status', 'produto_nome']

    def get_status(self, obj):
        return obj.get_status_display()