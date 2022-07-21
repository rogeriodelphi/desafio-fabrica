from django.contrib import admin

from produtos.models import Produto


class Produtos(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco', 'estoque', 'estoque_minimo', 'data_cadastro', 'ativo')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao', 'preco')
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10
    ordering = ['descricao']


admin.site.register(Produto, Produtos)