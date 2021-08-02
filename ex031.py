# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule a passagem, cobrando R$0,50 por KM para
# viagens de até 200 KM e R$0,45 para viagens mais longas.

distancia = int(input('Qual é a distância da sua viagem em KM? '))
if distancia <= 200:
    valor = distancia * 0.50
    print('Você terá que pagar R${:.2f}.'.format(valor))
else:
    valor2 = distancia * 0.45
    print('Você terá que pagar R${:.2f}.'.format(valor2))
print('Tenha uma boa viagem!')
