# Faça um programa que leia o nome completo de uma pessoa, mostrando em sequida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = str(input('Escreva seu nome: '))
n = nome.split()
print('Seu nome completo é {}.'.format(nome))
print('Seu primeiro nome é {}.'.format(n[0]))
print('Seu último nome é {}.'.format(n[len(n) - 1]))