# Faça um programa que leia a largura e a altura de uma parede em metros, calcule
# a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
# litro de tinta pinta uma área de 2m².

lar = float(input('Qual a largura da sua parede: '))
alt = float(input('Qual a altura da sua parede: '))
a = lar * alt
t = a / 2
print('Com uma parede de {}m e {}m e área de {}m² serão necessários {} litros de tinta para pintar a parede'.format(lar, alt, a, t ))