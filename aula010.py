# Parte teórica

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')
print('---FIM---')

# SIMPLIFICADO

tempo = int(input('Quantos anos tem seu carro? '))
print('Seu carro é novo!' if tempo <= 3 else 'Seu carro é velho!')
print('===FIM===')

#Parte prática

nome = str(input('Qual é seu nome? ')).strip().title()

if nome == 'Marcos':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 6.0:
    print('Sua nota foi {:.2f} e está na média, parabêns!'.format(m))
else:
    print('Sua nota foi {:.2f} e está abaixo da média, estude mais!'.format(m))