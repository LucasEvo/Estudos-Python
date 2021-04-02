# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Qual o preço do produto? R$ '))
desconto = p * (5/100)
pcd = p - desconto
print('O produto custava {} e agora custa {} com 5% de desconto.'.format(p, pcd))