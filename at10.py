# 10) Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

num = int(input('Insira o número que deseja calcular o !: '))
fat = 1
resultado = str(num) + '!= '

while num > 0:
    fat = num * fat
    if num == 1:
        resultado += '1 = ' + str(fat)
    else:
        resultado += str(num) + ' x '
    num -= 1
print(resultado)