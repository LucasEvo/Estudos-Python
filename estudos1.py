Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ('
       
SyntaxError: EOL while scanning string literal
>>> print(
	'
	
SyntaxError: EOL while scanning string literal
>>> print(
	'Hello World')
Hello World
>>> print(7+4)
11
>>> print('7'+'4')
74
>>> print 7  4
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(7  4)?
>>> print '7 4'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('7 4')?
>>> print(7 4)
SyntaxError: invalid syntax
>>> print('7 4')
7 4
>>> print('Olá, Mundo')
Olá, Mundo
>>> print (olá, mundo)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print (olá, mundo)
NameError: name 'olá' is not defined
>>> 7
7
>>> 4
4
>>> 7+4
11
>>> 74
74
>>> '7''4'
'74'
>>> print('Olá' + 5)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print('Olá' + 5)
TypeError: can only concatenate str (not "int") to str
>>> print ('Olá', 5)
Olá 5
>>> nome = Marcos
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    nome = Marcos
NameError: name 'Marcos' is not defined
>>> nome = 'Marcos'
>>> idade = 25
>>> peso = 74.6
>>> print(nome, idade, peso)
Marcos 25 74.6
>>> print(nome + idade + peso)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(nome + idade + peso)
TypeError: can only concatenate str (not "int") to str
>>> nome = input ('Qual seu nome?')
Qual seu nome?
>>> idade = input ('Qual sua idade?')
Qual sua idade?
>>> peso = input ('Qual seu peso')
Qual seu peso
>>> print (nome, idade, peso)
  
>>> 
================ RESTART: C:/Users/marco/Documents/ScriptsPython/teste01.py ================
Qual seu nome? Marcos
Qual sua idade? 25 anos
Qual seu peso? 74.6
 Marcos  25 anos  74.6
>>> 
================ RESTART: C:/Users/marco/Documents/ScriptsPython/teste01.py ================
Qual seu nome?lucas
Qual sua idade?43
Qual seu peso?88
lucas 43 88
>>> 