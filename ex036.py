# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela
# não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[33m-=\033[m' * 20)
print('           \033[34mCRÉDITO BANCÁRIO\033[m')
print('\033[33m-=\033[m' * 20)

casa = float(input('\nQual é o valor da casa? R$'))
salario = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos anos você quer pagar a casa? '))
prestacao = casa / (anos * 12)
excecao = salario * 30 / 100
print('Para pagar uma casa no valor de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(casa, anos, prestacao))


if prestacao <= excecao:
    print('\033[32mEmpréstimo Concedido\033[m')
else:
    print('\033[31mEmpréstimo Negado\033[m')

