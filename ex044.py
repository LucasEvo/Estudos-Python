# Elabore um programa que calcule o valor a ser pago por um produto, considerando o preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto;
# À vista no cartão: 5% de desconto;
# Em até 2x no cartão: preço normal;
# 3x ou mais no cartão: 20% de juros.

valor = float(input('Valor do produto: '))
pagamento = int(input('1 = À vista no dinheiro ou cheque\n2 = À vista no cartão\n3 = Até duas vezes no cartão\n4 = 3 vezes ou mais no cartão\nEscolha: '))

if pagamento == 1:
    print('Você deverá pagar {}.'.format(valor - (valor * 10 / 100)))
elif pagamento == 2:
    print('Você deverá pagar {}.'.format(valor - (valor * 5 / 100)))
elif pagamento == 3:
    print('Você deverá pagar {}.'.format(valor))
else:
    print('Você deverá pagar {}.'.format(valor + (valor * 20 / 100)))
