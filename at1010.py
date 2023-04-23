# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

cod1 = int(input('Códido da peça: '))
num1 = int(input('Número de peças: '))
val1 = float(input('Valor de cada peça: '))
print('Peça 2.')
cod2 = int(input('Códido da peça: '))
num2 = int(input('Número de peças: '))
val2 = float(input('Valor de cada peça: '))

sub1 = num1 * val1
sub2 = num2 * val2
tot = sub1 + sub2

print('VALOR A PAGAR: ', tot)