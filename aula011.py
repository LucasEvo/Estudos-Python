# Códigos para STYLE
# 0 none
# 1 BOLD
# 4 UNDERLINE
# 7 NEGATIVE

# Códigoa para TEXT
# 30 BRANCO
# 31 VERMELHO
# 32 VERDE
# 33 AMARELO
# 34 AZUL
# 35 MAGENTA
# 36 CIANO
# 37 CINZA

# Códigos para BACK
# 40 BRANCO
# 41 VERMELHO
# 42 VERDE
# 43 AMARELO
# 44 AZUL
# 45 MAGENTA
# 46 CIANO
# 47 CINZA


# \033['CODIGOS'm

# PARTE PRÁTICA

print('\033[33;44mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os \033[30mv\033[31ma\033[32ml\033[33mo\033[34mr\033[35me\033[36ms\033[m são \033[36m{}\033[m e \033[32m{}\033[m.'.format(a, b))
