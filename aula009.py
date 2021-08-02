#  PARTE TEÓRICA
frase = 'Curso em Vídeo Python'
print(frase)

# Fatiamento

print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# Análise

print(len(frase)) # TAMANHO DA STRING
print(frase.count('o')) # QUANTAS VEZES APARECE A LETRA PERGUNTADA
print(frase.count('o', 0, 13)) # CONTAGEM E FATIAMENTO AO MESMO TEMPO
print(frase.find('deo')) # MOSTRA A POSIÇÃO NA FRASE ONDE COMEÇOU A PALAVRA OU PEDAÇO DE PALAVRA PERGUNTADO
print(frase.find('Android')) # -1 SIGNIFICA QUE NÃO FOI ENCONTRADA A PALAVRA PERGUNTADA
print('Curso' in frase) # BUSCA SE É TRUE OU FALSE

# Transformação

print(frase.replace('Python', 'Android')) # MUDA UMA PALAVRA POR OUTRA
print(frase.upper()) # TRANSFORMA TODAS AS LETRAS EM MAIÚSCULAS
print(frase.lower()) # TRANSFORMA TODAS AS LETRAS EM MINÚSCULAS
print(frase.capitalize()) # TRANSFORMA SOMENTE A PRIMEIRA LETRA DA PRIMEIRA PALAVRA EM MAIÚSCULA
print(frase.title()) # TRANSFORMA A PRIMEIRA LETRA DE TODAS AS PALAVRAS DA FRASE EM MAIÚSCULA

frase2 = '  Aprenda Python  '
print(frase2)
print(len(frase2))
print(frase2.strip()) # TIRA TODOS OS ESPAÇOS DA ESQUERA E DA DIREITA DA FRASE
print(len(frase2.strip()))
print(frase2.rstrip())
print(frase2.lstrip())

# Divisão

print(frase.split())
print(len(frase.split()))

# Junção

print('-'.join(frase.split()))

# PARTE PRÁTICA

print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
texto = '''Fusce venenatis lorem ac aliquam cursus. Praesent tristique sem eget ipsum elementum suscipit. Aenean nibh ex, tincidunt non hendrerit
nec, efficitur sed justo. Pellentesque consequat lobortis mi a mattis. Morbi aliquam imperdiet orci a efficitur. Praesent ac gravida augue.
Mauris sit amet aliquam libero. Quisque tristique turpis est. Ut est mauris, semper in est nec, rhoncus egestas lacus. Nullam consectetur
cursus pulvinar. Aenean tristique id nunc in finibus. Nunc varius ligula nunc, eget suscipit lorem condimentum nec.'''
print(texto.count('o'))
print(len(texto))

frase3 = 'teste para ver se eu consigo dividir essa frase'
dividido = frase3.split()
print(dividido)
print(dividido[0])