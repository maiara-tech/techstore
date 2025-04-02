from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Sum
from django.utils import timezone
from django.db.models.functions import ExtractMonth
from .models import Produto
from .forms import ProdutoForm
from datetime import timedelta
from django.contrib.auth.decorators import login_required


#############################################
# PÁGINA INICIAL COM DASHBOARD
#############################################
def home(request):
    produtos = Produto.objects.all()

    # Estatísticas básicas
    total_produtos = produtos.count()
    produto_menor_estoque = produtos.order_by('quantidade_estoque').first()
    produto_mais_caro = produtos.order_by('-preco').first()

    # Gráfico de Estoque (dados reais)
    estoque_disponivel = produtos.filter(quantidade_estoque__gte=10).count()
    estoque_baixo = produtos.filter(quantidade_estoque__lt=10, quantidade_estoque__gt=0).count()
    estoque_zerado = produtos.filter(quantidade_estoque=0).count()

    # Gráfico de Cadastros (últimos 6 meses)
    meses_labels = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    cadastros_por_mes = [0] * 6

    seis_meses_atras = timezone.now() - timedelta(days=180)
    cadastros = (
        Produto.objects
        .filter(data_cadastro__gte=seis_meses_atras)
        .annotate(month=ExtractMonth('data_cadastro'))
        .values('month')
        .annotate(total=Count('id'))
        .order_by('month')
    )

    for item in cadastros:
        mes_index = item['month'] - 1
        if 0 <= mes_index < 6:
            cadastros_por_mes[mes_index] = item['total']

    context = {
        'total_produtos': total_produtos,
        'produto_menor_estoque': produto_menor_estoque,
        'produto_mais_caro': produto_mais_caro,
        'vendas_totais': produtos.aggregate(Sum('vendas'))['vendas__sum'] or 0,
        'estoque_disponivel': estoque_disponivel,
        'estoque_baixo': estoque_baixo,
        'estoque_zerado': estoque_zerado,
        'cadastros_por_mes': cadastros_por_mes,
        'meses_labels': meses_labels,
    }
    return render(request, 'portal/home.html', context)


#############################################
# PÁGINAS SECUNDÁRIAS
#############################################
def sobre(request):
    return render(request, 'portal/sobre.html')


def contato(request):
    return render(request, 'portal/contato.html')


#############################################
# CRUD DE PRODUTOS
#############################################
def listar_produtos(request):
    produtos = Produto.objects.all().order_by('nome')
    return render(request, 'portal/listar_produtos.html', {'produtos': produtos})


@login_required
def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.user
            produto.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'portal/criar_produto.html', {'form': form})


@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'portal/editar_produto.html', {'form': form, 'produto': produto})


@login_required
def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == "POST":
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'portal/excluir_produto.html', {'produto': produto})


#############################################
# PAINEL ADMIN (OPCIONAL)
#############################################
@login_required
def painel_admin(request):
    produtos = Produto.objects.all()
    total_produtos = produtos.count()
    valor_total_estoque = sum(produto.preco * produto.quantidade_estoque for produto in produtos)

    context = {
        'produtos': produtos,
        'total_produtos': total_produtos,
        'valor_total_estoque': valor_total_estoque,
    }
    return render(request, 'portal/painel_admin.html', context)