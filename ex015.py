# Escreva um programa que pergunte a quantidade de KM percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
# por KM rodado.

km = float(input('Indique a quantidade de KM rodado: '))
dias = int(input('Indique quantos dias você usou o carro: '))
vkm = km * 0.15
vdias = dias * 60
total = vkm + vdias
print('Com {}KM rodados e {} dias alugando o carro o total a ser pago é {} reais.'.format(km, dias, total))