# Condições Aninhadas

# PRÁTICA

nome = str(input('Qual é seu nome? '))
if nome == 'Marcos':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))