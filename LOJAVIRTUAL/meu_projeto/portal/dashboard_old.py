from dash import dcc, html
import plotly.express as px
from django_plotly_dash import DjangoDash
from portal.models import Produto  # Importando os produtos reais do Django

# Criando um app Dash dentro do Django
app = DjangoDash('Dashboard')

# Buscando os dados do banco
produtos = Produto.objects.all()
nomes = [p.nome for p in produtos]
estoques = [p.quantidade_estoque for p in produtos]

# Criando gráfico de produtos por estoque
fig = px.bar(
    x=nomes,
    y=estoques,
    title="Estoque de Produtos",
    labels={"x": "Produto", "y": "Quantidade em Estoque"},
)

# Layout do Dashboard
app.layout = html.Div(children=[
    html.H3("Dashboard de Produtos"),
    dcc.Graph(figure=fig),
    dcc.Store(id='store-data'),
])
