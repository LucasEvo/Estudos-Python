# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1- O nome com todas a letras minúsculas
# 2- O nome com todas a letras maiúsculas
# 3- Quantas letras ao todo (sem considerar espaços).
# 4- Quantas letras tem o primeiro nome.

nome = str(input('Qual seu nome completo? R: ')).strip()
print('Seu nome é {}.'.format(nome))
print('Seu nome com todas as letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é {}.'.format(nome.lower()))
print('Seu nome todo tem {} letras.'.format(len(nome) - nome.count(' ')))
primeiro_nome = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(primeiro_nome[0])))
