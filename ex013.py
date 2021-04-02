# Faça um programa que leia o salário de um funcionário e mostre seu novo saláro com 15% de aumento.

sal = float(input('Qual seu salário? R$ '))
sca = sal + (sal * 15 / 100)
print('Seu salário era {} Reais e com o aumento de 15% passou a ser {} Reais.'.format(sal, sca))