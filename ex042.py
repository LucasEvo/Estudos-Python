# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.
# Equilátero: todos os lados iguais.
# Isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes.

print('+-' * 20)
print('Analisador de triângulos 2.0')
print('+-' * 20)

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {}, {} e {} formam um triângulo.'.format(r1, r2, r3))
    if r1 == r2 == r3:
        print('Este é um triângulo Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este é um triângulo Isósceles.')
    else:
        print('Este é um triângulo Escaleno.')
else:
    print('Essas retas não formam um triângulo.')
