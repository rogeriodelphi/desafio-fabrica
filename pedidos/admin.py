from django.contrib import admin

from pedidos.models import Pedido


class Pedidos(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'quantidade', 'ativo', 'criado_em')
    list_display_links = ('id', 'cliente')
    search_fields = ('cliente', 'quantidade')
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10
    # ordering = ('item.produto',)


admin.site.register(Pedido, Pedidos)
