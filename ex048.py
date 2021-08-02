# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de 3 e que se encontram  no
# intervalo de 1 até 500.

s = 0
for c in range(0, 500, 3):
    print(c)
    i = int(c)
    s = s + i
print('O somatório dos números múltiplos de 3 de 1 a 500 é {}.'.format(s))
