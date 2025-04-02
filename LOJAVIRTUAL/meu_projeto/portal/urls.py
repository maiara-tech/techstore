from django.urls import path
from .views import (
    home, listar_produtos, criar_produto, editar_produto,
    excluir_produto, painel_admin, sobre, contato
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),  # Página inicial
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('produtos/criar/', criar_produto, name='criar_produto'),
    path('produtos/editar/<int:produto_id>/', editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:produto_id>/', excluir_produto, name='excluir_produto'),
    path('admin/', painel_admin, name='painel_admin'),

    # URLs de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='portal/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Novas páginas
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),

]
