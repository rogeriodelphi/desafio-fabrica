from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from produtos.models import Produto
from produtos.serializers import ProdutoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProdutosViewSet(viewsets.ModelViewSet):
    """Listando produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['produto']
    search_fields = ['produto', 'preco']
    filterset_fields = ['ativo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]