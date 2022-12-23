from django.contrib.auth.models import User
from django.db import models


class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    descricao = models.TextField('Descrição')

    def __str__(self):
        return f'{self.nome}'


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=150)
    email = models.CharField('E-mail', max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.nome}  {self.sobrenome}'
