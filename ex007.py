# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = int(input('Escreva a primeira nota: '))
n2 = int(input('Escreva a segunda nota: '))
s = (n1 + n2)/2

print('Como as notas são {} e {}, a média é {}'.format(n1, n2, s))

# Resolução do exercício CLEAN CODE:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
#s = (n1 + n2) / 2
#print('A média foi {}'.format(s))
print('A média foi {}'.format((n1+n2)/2))