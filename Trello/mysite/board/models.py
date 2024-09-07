from django.db import models

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome


class Tarefas(models.Model):
    idTarefa = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    situacao = models.IntegerField()

    def __str__(self):
        return self.titulo
