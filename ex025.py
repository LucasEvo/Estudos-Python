# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Qual seu nome? ')).strip().title()
print('Seu nome tem Silva?', 'Silva' in nome)