### Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

a = float(input('Insira a nota da AV1: '))*0.35
b = float(input('Insira a nota da AV2: '))*0.75
p = 0
m = a + b
if m > 10:
    print('MEDIA = 10')
else:
    print('MEDIA = ', m)