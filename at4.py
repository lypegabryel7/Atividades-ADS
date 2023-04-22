"""4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
terminar quando for lido um número negativo. """

pri = 0
seg = 0
ter = 0
qua = 0

while True:
    num = float(input('Insira um número: '))
    if num < 26 and num >= 0:
        pri += 1
    elif num < 51 and num >= 26:
        seg += 1
    elif num < 76 and num >= 51:
        ter += 1
    elif num <= 100 and num >= 76:
        qua += 1
    if num < 0:
        break
print(f'A quantidade de números entre 0-25 foi: {pri}')
print(f'A quantidade de números entre 26-50 foi: {seg}')
print(f'A quantidade de números entre 51-75 foi: {ter}')
print(f'A quantidade de números entre 76-100 foi: {qua}')
