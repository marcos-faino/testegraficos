# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Autor(models.Model):
    idautor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'


class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Editora(models.Model):
    ideditora = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    fone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editora'


class Escreve(models.Model):
    idlivro = models.IntegerField(primary_key=True)
    idautor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'escreve'
        unique_together = (('idlivro', 'idautor'),)


class Genero(models.Model):
    idgenero = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'genero'


class ItensDaVenda(models.Model):
    idvenda = models.IntegerField(primary_key=True)
    idlivro = models.IntegerField()
    qtd = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itens_da_venda'
        unique_together = (('idvenda', 'idlivro'),)


class Livro(models.Model):
    idlivro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    preco = models.FloatField(blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    idgenero = models.IntegerField()
    ideditora = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'livro'


class Venda(models.Model):
    idvenda = models.AutoField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    idcliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'venda'
