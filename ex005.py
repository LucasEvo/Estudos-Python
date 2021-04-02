#1 - Faça um programa que leia um número inteiro e mostre na tela o seu
#sucessor e seu antecessor.

n = int(input('Escreva um número: '))
suc = n + 1
ant = n - 1
print('O número é: {}, seu sucessor é: {} e seu antecessor é: {}.'.format(n, suc, ant))

# Resolução do exercício CLEAN CODE:
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}.'.format(n, (n - 1), (n + 1)))


















