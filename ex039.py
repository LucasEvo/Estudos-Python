# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar;
# - Se é a hora de se alistar;
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date

nascimento = int(input('Qual ano voce nasceu? '))
ano = date.today().year
print(ano)
if ano - nascimento < 18:
    print('Voce ainda não precisa se alistar.')
    print('Ainda faltam {} anos para voce se alistar.'.format((nascimento + 18) - ano))
elif ano - nascimento == 18:
    print('Está na hora de voce se alistar.')
else:
    print('Já passou da hora de voce se alistar.')
    print('Voce devia ter se alistado há {} anos.'.format(ano - (nascimento + 18)))
