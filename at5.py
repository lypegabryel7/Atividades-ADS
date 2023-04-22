"""5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
números lidos. O número que encerrará a leitura será zero. """

numpar = 0
numimp = 0
somaimp = 0
somapar = 0

while True:
    num = float(input('Insira um número positivo: '))
    if num % 2 == 0:
        numpar += 1
        somapar += num
    elif num % 2 != 0:
        numimp += 1
        somaimp += num
    if num <= 0:
        break

quant = numimp + numpar
soma = somaimp + somapar
print(f'A quantidade de números ímapares é: {numimp}, e pares é: {numpar}.')
print(f'A média dos números pares é: {somapar/numpar}.')
print(f'A média geral é: {soma/quant}')