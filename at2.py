""" 2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
mostrar :
a. A menor altura do grupo;
b. A maior altura do grupo; """

maioraltura = 0
menoraltura = 500
for a in range(1, 16):
    altura = float(input(f'Insira uma altura {a}: '))
    if altura > maioraltura:
        maioraltura = altura
    if altura < menoraltura:
        menoraltura = altura
print(f'A maior altura é: {maioraltura}')
print(f'A menor altura é: {menoraltura}')