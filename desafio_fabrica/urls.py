from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clientes.views import ClientesViewSet
from produtos.views import ProdutosViewSet
from pedidos.views import PedidosViewSet

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet)
router.register('produtos', ProdutosViewSet)
router.register('pedidos', PedidosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
