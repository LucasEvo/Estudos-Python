# Crie um programa que faça o computador jogar JOKENPÔ com você.

import random
from time import sleep

jogador = int(input('Escolhe sua jogada:\n1 - Pedra\n2 - Papel\n3 - Tesoura\nEscolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
computador = [1, 2, 3]
escolha = random.choice(computador)

if jogador == 1 and escolha == 1:
    print('Você escolheu Pedra e o computador também.')
    print('Empatou!')
elif jogador == 1 and escolha == 2:
    print('Você escolheu Pedra e o computador Papel.')
    print('Computador ganhou!')
elif jogador == 1 and escolha == 3:
    print('Você escolheu Pedra e o computador Tesoura.')
    print('Jogador ganhou!')
elif jogador == 2 and escolha == 1:
    print('Você escolheu Papel e o computador Pedra.')
    print('Jogador ganhou!')
elif jogador == 2 and escolha == 2:
    print('Você escolheu Papel e o computador também.')
    print('Empatou!')
elif jogador == 2 and escolha == 3:
    print('Você escolheu Papel e o computador Tesoura.')
    print('Computador ganhou!')
elif jogador == 3 and escolha == 1:
    print('Você escolheu Tesoura e o computador Pedra.')
    print('Computador ganhou!')
elif jogador == 3 and escolha == 2:
    print('Você escolheu Tesoura e o computador papel.')
    print('Jogador ganhou!')
elif jogador == 3 and escolha == 3:
    print('Você escolheu Tesoura e o computador também.')
    print('Empatou!')
else:
    print('Jogada inválida')


