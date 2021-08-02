# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é o maior;
# - O segundo valor é o maior;
# Não existe valor maior, os dois são iguais.

print('-+' * 12)
print('Comparativo de números')
print('-+' * 12)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print('{} é o maior número.'.format(n1))
elif n2 > n1:
    print('{} é o maior número.'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais.')

