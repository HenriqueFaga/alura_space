from django.db import models
from datetime import datetime 

class Fotografia(models.Model):
    # Colunas:

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    # CharField -> String;
    # max_length maximo de char.
    # null=False nao pode ser nulo.
    # blank=False nao pode ser string vazia!
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    # TextField -> campo de texto
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="foto/%Y/%m/%d/", blank=True)
    categoria = models.CharField(max_length=150, choices=OPCOES_CATEGORIA, default='')
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        # Boa pratica, devolve o nome de cada um dos itens.
        return self.nome
