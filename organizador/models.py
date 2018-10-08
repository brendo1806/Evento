from django.db import models


class Organizador(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
         return self.nome


