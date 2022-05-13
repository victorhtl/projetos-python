from random import randint

humano = 0
maquina = 0
rodada = 1

while rodada < 4:
    print(f'\033[;1;34mRodada {rodada}\033[m')

    itens = ('Pedra', 'Papel', 'Tesoura')

    while True:
        jogador = int(input('0-Pedra 1-Papel 2-tesoura: '))
        if jogador <= 2:
            break
        else:
            print('Entrada inválida')
    adversario = randint(0, 2)

    print("/" * 20)
    print(f'Jogador: {itens[jogador]}')
    print(f'Máquina: {itens[adversario]}')

    print("/" * 20)
    if jogador == adversario:
        print('\033[;1mEMPATE\033[m')
        continue
    elif jogador == 0 and adversario == 2 or jogador == 1 and adversario == 0 or jogador == 2 and adversario == 1:
        humano += 1
    else:
        maquina += 1

    print('Placar: ')
    print(f'Jogador: {humano}')
    print(f'Máquina: {maquina} ')
    print()
    rodada += 1

if humano > maquina:
    print('\033[;1;32mVOCÊ VENCEU')
else:
    print('\033[;1;31mVOCÊ PERDEU')