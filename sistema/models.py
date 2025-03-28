from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateField()
    ativo = models.BooleanField()
    status = models.BooleanField()

    def __str__(self):
        return self.nome

class Filme(models.Model):
    nome_do_filme = models.CharField(max_length=100)
    ano_lancamento = models.DateField()
    estudio = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    sinopse = models.TextField()
    data_cadastro = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nome_do_filme

class Genero(models.Model):
    nome_genero = models.CharField(max_length=100)
    data_cadastro = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nome_genero