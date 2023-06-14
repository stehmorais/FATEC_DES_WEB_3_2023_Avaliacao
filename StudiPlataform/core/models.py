from django.db import models

class RegistroModel(models.Model):
    nome = models.CharField('Nome Aluno', max_length=100)
    OPCOES_PROFESSOR = (
        ('Orlando Saraiva Jr', 'Orlando Saraiva Jr'),
        ('Thiago Mendes', 'Thiago Mendes'),
        ('Nilton', 'Nilton'),
        ('Sandro', 'Sandro'),
        ('Esdras', 'Esdras'),
        ('Ana Celia', 'Ana Celia'),
    )
    professor = models.CharField('Nome do Professor', max_length=100, choices=OPCOES_PROFESSOR)

    def __str__(self):
        return self.nome