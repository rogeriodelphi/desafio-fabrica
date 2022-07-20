from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clientes.views import ClientesViewSet
from produtos.views import ProdutosViewSet
from pedidos.views import PedidosViewSet, ListaPedidosCliente, ListaPedidosProduto

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('produtos', ProdutosViewSet, basename='Produtos')
router.register('pedidos', PedidosViewSet, basename='Pedidos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/pedidos/', ListaPedidosCliente.as_view()),
    path('produto/<int:pk>/pedidos/', ListaPedidosProduto.as_view()),
]
