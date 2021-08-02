# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input('Qual cidade você mora: ')).strip().title()
print('Se sua cidade começa com a palavra "Santo" vai aparecer "True" e se não começa vai aparecer "False".')
print('Santo' in cidade)
