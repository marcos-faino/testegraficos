from django.contrib import admin
from .models import *


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone']


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ['nome', 'fone']


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['descricao']


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'preco', 'estoque', 'idgenero', 'ideditora']


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['data', 'total', '_cliente']

    def _cliente(self, instance):
        return Cliente.objects.get(idcliente=instance.idcliente)