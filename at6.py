# 6) Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.


i = 0

for i in range (100, 201):
    if i % 2 != 0:
        print(i)