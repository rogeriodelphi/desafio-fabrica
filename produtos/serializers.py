from rest_framework import serializers
from produtos.models import Produto
# from produtos.validators import *


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'