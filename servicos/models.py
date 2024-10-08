from django.db import models
from clientes.models import Cliente
from .choices import ChoicesCategoriaManutencao
from secrets import token_hex
from datetime import datetime

class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=3, choices=ChoicesCategoriaManutencao.choices)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.titulo

class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    categoria_manutencao = models.ManyToManyField(CategoriaManutencao)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_inicio = models.DateTimeField(null=True)
    data_entrega = models.DateTimeField(null=True)
    finalizado = models.BooleanField(default=False)
    protocolo = models.CharField(max_length=52, unique=True, editable=False)

    def __str__(self) -> str:
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.protocolo:
            self.protocolo = datetime.now().strftime('%d_%m_%Y_%H_%M_%S_') + token_hex(16)
        super().save(*args, **kwargs)

    def preco_total(self):
        preco_total = float(0)
        for categoria in self.categoria_manutencao.all():
            preco_total += float(categoria.preco)
        return preco_total
