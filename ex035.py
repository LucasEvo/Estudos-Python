# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não3 formar um triângulo.

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
n1 = float(input('Primeira reta: '))
n2 = float(input('Segunda reta: '))
n3 = float(input('Terceira reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Forma um triângulo.')
else:
    print('Não forma um triângulo.')
print('-=' * 20)