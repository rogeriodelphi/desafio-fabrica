from rest_framework import serializers
from pedidos.models import Pedido
# from pedidos.validators import *


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'