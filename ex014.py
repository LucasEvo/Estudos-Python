# Escreva um programa que converta uma temperatura digitada em °C e converta em °F.

c = float(input('Escreva a temperatura em °C: '))
f = (c * 9 / 5) + 32
print('A temperatura {}°C convertida é {}°F.'.format(c, f))
