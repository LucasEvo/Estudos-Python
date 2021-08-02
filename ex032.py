'''import calendar

ano = int(input('Qual ano você gostaria de saber se é bissexto? '))
if calendar.isleap(ano):
    print('Este é um ano bissexto!')
else:
    print('Este não é um ano bissexto.')'''


from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} Não é Bissexto!'.format(ano))
