from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from pedidos.models import Pedido
from pedidos.serializers import PedidoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class PedidosViewSet(viewsets.ModelViewSet):
    """Listando pedidos"""
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['item']
    search_fields = ['item', 'quantidade']
    filterset_fields = ['ativo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]