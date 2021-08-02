# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# - Média abaixo de 5.0: REPROVADO;
# - Média entre 5.0 e 6.9: RECUPERAÇÂO;
# - Média 7.0 ou superior: APROVADO.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Voce foi reprovado pois sua nota foi {}.'.format(media))
elif media > 5.0 and media < 6.9:
    print('Voce está de recuperação pois sua nota foi {}.'.format(media))
elif media <= 7.0:
    print('Voce foi aprovado já que sua nota foi {}.'.format(media))

