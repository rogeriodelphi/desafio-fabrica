from django.contrib import admin

from produtos.models import Produto


class Produtos(admin.ModelAdmin):
    list_display = ('id', 'produto', 'preco', 'estoque', 'estoque_minimo', 'data', 'ativo')
    list_display_links = ('id', 'produto')
    search_fields = ('produto', 'preco')
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10
    ordering = ('produto',)


admin.site.register(Produto, Produtos)