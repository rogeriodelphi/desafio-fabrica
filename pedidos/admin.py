from django.contrib import admin

from pedidos.models import Pedido


class Pedidos(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'quantidade', 'status', 'criado_em')
    list_display_links = ('id', 'cliente')
    search_fields = ('cliente', 'quantidade', 'criado_em')
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 10
    # ordering = ('item.produto',)


admin.site.register(Pedido, Pedidos)
