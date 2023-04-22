# 1) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.

soma = 0
for i in range (3, 501, 3):
    if i % 2 != 0:
        soma += i
print(f'a soma dos números é: {soma}')
