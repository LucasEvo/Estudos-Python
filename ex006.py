# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

n = int(input('Escreva um número: '))
dobro = n * 2
triplo = n * 3
rq = n ** 2

print('O número que você escreveu é: {}, seu dobro é: {} , seu triplo é: {} e sua raiz quadrada é: {}'.format(n, dobro, triplo, rq))

# Resolução do exercício CLEAN CODE:

n = int(input('Digite um número: '))
print('O número que você digitou foi {}.\nSeu dobro é {}.\nSeu triplo é {}.\nSua raiz quadrada é {:.2f}.'.format(n, (n * 2), (n * 3), (n ** (1/2))))
