# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O pragrama deverá escrever na tela se o usuário venceu ou perdeu.

import random
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 30)
chute = int(input('Qual número eu pensei? ')) # Palpite do jogador
num = random.randint(0, 5) # Sorteio do número
if chute == num:
    print('Eu pensei no número {} e você acertou!'.format(num))
else:
    print('Eu não pensei nesse número e você errou!')
print('-=' * 20)
print('               FIM DE JOGO')
print('-=' * 20)