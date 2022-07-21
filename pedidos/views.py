from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, generics

from pedidos.models import Pedido
from pedidos.serializers import PedidoSerializer, ListaPedidosClienteSerializer, ListaPedidosProdutoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class PedidosViewSet(viewsets.ModelViewSet):
    """Listando pedidos"""
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['descricao']
    search_fields = ['descricao', 'valor_total']
    filterset_fields = ['status']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaPedidosCliente(generics.ListAPIView):
    """"Listando os pedidos de um(a) cliente"""
    def get_queryset(self):
        queryset = Pedido.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPedidosClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaPedidosProduto(generics.ListAPIView):
    """Listando todos os pedidos para um determinado produto """
    def get_queryset(self):
        queryset = Pedido.objects.filter(produto=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPedidosProdutoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]