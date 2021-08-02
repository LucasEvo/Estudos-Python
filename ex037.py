# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# binário, octal ou hexadecimal.

n = int(input('Escreva um número: '))
escolha = int(input('1 = Binário\n2 = Octal\n3 = Hexadecimal\nEscolha: '))

if escolha == 1:
    print('O número {} em binário é {:b}.'.format(n, n))
elif escolha == 2:
    print('O número {} em octal é {:o}.'.format(n, n))
else:
    print('O número {} em hexadecimal é {:x}.'.format(n, n))


