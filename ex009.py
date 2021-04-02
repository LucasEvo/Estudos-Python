# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Escreva um número inteiro: '))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print('A tabuada deste número é:\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n'.format(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10))

# Resolução do exercício em CLEAN CODE:

n = int(input('Escreva um número inteiro para ver sua tabuada: '))
print('-' * 12)
print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x {:2} = {}'.format( n, n * 1, n, n * 2, n, n * 3, n, n * 4, n, n * 5, n, n * 6, n, n * 7, n, n * 8, n, n * 9, n,10, n * 10))
print('-' * 12)