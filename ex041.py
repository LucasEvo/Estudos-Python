# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Júnior
# Até 20 anos: Senior
# Acima de 20 anos: Master

from datetime import date
nascimento = int(input('Qual ano voce nasceu? '))
ano = date.today().year

if ano - nascimento <= 9:
    print('Sua categoria é Mirim.')
elif ano - nascimento > 9 and ano - nascimento <= 14:
    print('Sua categoria é Infantil.')
elif ano - nascimento > 14 and ano - nascimento < 20:
    print('Sua categoria é Júnior.')
elif ano - nascimento > 19 and ano - nascimento < 21:
    print('Sua categoria é Senior.')
elif ano - nascimento > 20:
    print('Sua categoria é Master.')
