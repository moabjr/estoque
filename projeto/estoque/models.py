from django.contrib.auth.models import User
from django.db import models
from projeto.core.models import TimeStempedModel
from projeto.produto. models import Produto

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)

class Estoque(TimeStempedModel):
    funcionario = models.ForeingKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.pk )

class EstoqueItens(models.Model):
    estoque = models.ForeingKey(Estoque, on_delete=models.CASCADE)
    produto = models.ForeingKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{}-{}-{}'.format(self.pk, self.estoque.pk, self.produto)
