from django.contrib import admin

from pedidos.models import Pedido


class Pedidos(admin.ModelAdmin):
    list_display = ('id', 'data_pedido', 'cliente', 'status', 'criado_em')
    list_display_links = ('id', 'cliente')
    search_fields = ('cliente', 'valor_total', 'data_pedido')
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 10
    # ordering = ('produto.produto',)


admin.site.register(Pedido, Pedidos)
