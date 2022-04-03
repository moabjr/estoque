import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from projeto.produto.models import Produto


class Utils:
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits)for i in range(max_length)))


class ProdutoClass:
    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                importado=choice((True,False)),
                ncm=Utils.gen_digits(8),
                preco=random()*randint(10,50),
                estoque= randint(10,200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    'Apontador',
    'Caderno 100 folhas',
    'Caderno capa dura 200 folhas',
    'Caneta esferografica azul',
    'Caneta esferografica preta',
    'Caneta esferografica vermelha',
    'Durex',
    'Giz de cera 12 cores',
    'Lapiseira 0.3mm',
    'Lapiseira 0.5mm',
    'Lapiseira 0.7mm',
    'Lapis de cor 24 cores',
    'Lapis',
    'Papel sulfite A4 pacote com 100 folhas',
    'Pasta elastica'
    'Tesoura',

)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)

toc = timeit.default_timer()

print('Tempo: ', toc -tic)