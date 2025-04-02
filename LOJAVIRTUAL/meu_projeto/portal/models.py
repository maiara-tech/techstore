from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    # Apenas o novo campo vendas (sem categoria)
    vendas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome