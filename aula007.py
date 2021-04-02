# Símbolos aritméticos
# + = Adição
# - = Subtração
# * = Multiplicação
# / = Divisão
# ** = Potência
# // = Divisão inteira
# % = Resto da Divisão

# Ordem de Precedência = (), **, * e / e // e %, + e -
# 1 = ()
# 2 = **
# 3 = *, /, //, %
# 4 = +, -

a = 5+3*2
print(a)

b = 3*5+4**2
print(b)

c = 3*(5+4)**2
print(c)

d = 'oi' + 'olá'
print(d)

e = 'oi' * 5
print(e)

f = '=' * 20
print(f)

#nome = input('Qual é seu nome?')
#print('Prazer em te conhecer,{}!'.format(nome))
#print('Prazer em te conhecer,{:<20}!'.format(nome))
#print('Prazer em te conhecer,{:>20}!'.format(nome))
#print('Prazer em te conhecer,{:^20}!'.format(nome))
#print('Prazer em te conhecer,{:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))

n3 = int(input('Um valor: '))
n4 = int(input('Outro valor: '))
s = n3 + n4
m = n3 * n4
d = n3 / n4
di = n3 // n4
e = n3 ** n4
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d))
print('A divisão inteira é {} e potência é {}'.format(di, e))

#Para quebrar print colocar \n
#Para não quebrar colocar no final do print (, end='')

