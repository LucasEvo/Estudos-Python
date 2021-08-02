# Faça um programa que leia uma frase pelo teclado e mostre:
# 1- Quantas vezes aparece a letra 'A'
# 2- Em que posição ela aparece a primeira vez
# 3- Em que posição ele aparece a última vez

frase = str(input('Escreva uma frase: ')).strip().upper()
contador = frase.count('A')
primeira = frase.find('A') + 1
ultima = frase.rfind('A') + 1
print('Na frase que você escreveu aparecem {} vezes a letra "A".'.format(contador))
print('A letra "A" apareceu a primeira vez na posição {}.'.format(primeira))
print('A letra "A" aparece a última vez na posição {}.'.format(ultima))
