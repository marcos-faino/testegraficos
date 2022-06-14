from django.db import models


class Autor(models.Model):
    idautor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Cliente'

    def __str__(self):
        return self.nome


class Editora(models.Model):
    ideditora = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    fone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editora'
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'

    def __str__(self):
        return self.nome


class Genero(models.Model):
    idgenero = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'genero'
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

    def __str__(self):
        return self.descricao


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
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo


class Venda(models.Model):
    idvenda = models.AutoField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    idcliente = models.IntegerField()

    class Meta:
        managed = False
        db_table = "venda"
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"

    def __str__(self):
        return self.idvenda
