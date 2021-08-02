# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual seu salário? R$ '))
aumento1 = sal * (10 / 100)
salsuperior = sal + aumento1
aumento2 = sal * (15 / 100)
salinferior = sal + aumento2
if sal > 1250:
    print('Seu novo salário é R$ {:.2f}.'.format(salsuperior))
if sal <= 1250:
    print('Seu novo salário é R$ {:.2f}.'.format(salinferior))
