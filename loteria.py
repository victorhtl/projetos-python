"""
Você insere a quantidade e o range dos números
Retorna os numeros selecionados
"""
from random import randint


def loteria(qtde, inicio, fim):
    """
    qtde - quantidade de numeros a serem sorteados
    inicio - a partir de qual numero
    fim - ate qual numero
    """
    sorteados = []
    for i in range(0, qtde):
        num_sorteado = randint(inicio, fim)
        if num_sorteado not in sorteados:
            sorteados.append(num_sorteado)

    print(f'Os sorteados foram {sorteados}')


loteria(6, 0, 100)
