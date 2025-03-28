from django.contrib import admin

from sistema.models import Filme, Genero, Usuario

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'telefone', 'email', 'endereco', 'data_cadastro', 'ativo', 'status')
    list_filter = ('ativo', 'status')

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('nome_do_filme', 'ano_lancamento', 'estudio', 'genero', 'sinopse', 'data_cadastro',)
    list_filter = ('ano_lancamento', 'estudio', 'genero')

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome_genero', 'data_cadastro',)
    list_filter = ('data_cadastro',)
    