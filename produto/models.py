from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=12)
    descricao = models.CharField(max_length=12)
    fornecedor = models.CharField(max_length=12)

    def __str__(self):
        return self.nome_produto
    
