# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem das apresentações é ')
print(lista)