# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere 1 dólar = 3,27 reais.

r = float(input('Quantos reais você tem? R: R$ '))
d = r / 5.80
print('Você pode comprar {:.2f} dólares com a quantidade de reais que você informou!'.format(d))