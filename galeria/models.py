from django.db import models

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
    descriacao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=150, choices=OPCOES_CATEGORIA, default='')

    def __str__(self):
        # Boa pratica, devolve o nome de cada um dos itens.
        return f"Fotografia [nome={self.nome}]"
