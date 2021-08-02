# Escreva um progrma que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

vel = float(input('Qual a velocidade do carro? '))
multa = (vel - 80) * 7
print('-=-' * 12)
if vel > 80:
    print('Você está acima da velocidade e foi multado!')
    print('Sua multa é de R${:.2f}.'.format(multa))
else:
    print('Você está na velocidade permitida! Boa Viagem!')
print('-=-' * 12)
