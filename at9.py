# 9) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.G. contendo 10 valores.

a = int(input('Insira o vaor inicial: '))
r = int(input('Insira a razão: '))

for c in range(1, 11):
    print(f'{a} -> ', end='')
    a *= r
print('End')