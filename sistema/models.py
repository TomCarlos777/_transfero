from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='imagens/%Y/%m')
    status = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Genero(models.Model):
    nome_genero = models.CharField(max_length=50)
    data_cadastro = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nome_genero

class Filme(models.Model):
    nome_do_filme = models.CharField(max_length=50)
    ano_lancamento = models.DateField(default=timezone.now)
    estudio = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    # genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    sinopse = models.TextField()
    data_cadastro = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nome_do_filme


    


# PK -> Primary Key -> Chave Primária.
# FK -> Foreign Key -> Chave Estrangeira.
