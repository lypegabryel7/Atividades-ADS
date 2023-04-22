""" 3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
negativos e o percentual de valores negativos e positivos. """

qntpositiva = 0
qntnegativa = 0
quantidade = 0
soma = 0
val = 0
while val != 666:
    val = float(input('Insira um número (digite "666" p/ encerrar): '))
    if val < 0:
        quantidade += 1
        qntnegativa += 1
        soma += val
    elif val >= 0:
        quantidade += 1
        qntpositiva += 1
        soma += val

total = qntnegativa + qntpositiva
media = soma / quantidade
perneg = qntnegativa * 100 / total
perpos = qntpositiva * 100 / total

print(f'A média dos valores foi: {media}')
print(f'A quantidade de valores positivos foram: {qntpositiva}, e os valores negativos foram: {qntnegativa}.')
print(f'O percentual entre ambos foram {perpos}% de positivos e {perneg}% de negativos.')