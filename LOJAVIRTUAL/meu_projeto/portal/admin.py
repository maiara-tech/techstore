from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade_estoque', 'data_cadastro')  # Campos exibidos
    search_fields = ('nome',)  # Campo de busca
    list_filter = ('data_cadastro',)  # Filtros laterais
    ordering = ('-data_cadastro',)  # Ordenação padrão

# Personalização do Django Admin
admin.site.site_header = "Painel de Administração da Loja"
admin.site.site_title = "Administração da Loja"
admin.site.index_title = "Bem-vindo ao painel de controle"



