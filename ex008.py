# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Escreva quantos metros você gostaria de converter: '))
cm = m * 100
mm = m * 1000
print('O valor convertido em centímetros e milímetros é, respectivamente: {} cm e {} mm'.format(cm, mm))

# KM HM DAM M DM CM MM

# Resolução do exercício CLEAN CODE:

m = float(input('Escreva uma quantidade de metros: '))
print('O valor {} m convertido em todas as medidas é:\n{} km,\n{} hm,\n{} dam,\n{} dm,\n{} cm,\n{} mm'.format(m, m / 1000, m / 100, m / 10, m * 10, m * 100, m * 1000))
