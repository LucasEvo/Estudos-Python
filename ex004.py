n = input('Digite algo:')
print('O tipo primitivo desse valor é', type(n))
print('É alfanumérico?', n.isalnum())
print('É número?', n.isnumeric())
print('É letra?', n.isalpha())
print('Está maiúsculo?', n.isupper())
print('Está minúsculo?', n.islower())