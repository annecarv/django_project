from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.nome

class Carro(models.Model):
    carro = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    ano = models.IntegerField(max_length=4)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.carro