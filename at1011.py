# Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.

print('Calcular o volume de uma esfera: (4/3)*pi*R³.')
raio = int(input('Insira o raio(R): '))
tot = (4/3) * 3.14159 * raio**3

print('VOLUME = ', tot)