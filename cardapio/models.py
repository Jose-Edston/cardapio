from django.db import models

class Usuario(models.Model):

    name = models.CharField(max_length=50)

    email = models.EmailField()

    telefone = models.CharField(max_length=30)

    data_criacao = models.DateField(default=None, null=True)

    peso = models.CharField(max_length=5)

    altura = models.CharField(max_length=5)

    idade = models.CharField(max_length=3)

class CardapioCliente(models.Model):

    refeicao = models.CharField(max_length=500)

    porcao = models.CharField(max_length=20)

    horario = models.CharField(max_length=10)

    tipo_refeicao = models.CharField(max_length=50)

