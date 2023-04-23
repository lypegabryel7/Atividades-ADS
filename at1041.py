# Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

x = float(input('Insira o primeiro valor: ')) 
y = float(input('Insira o segundo valor: ')) 
if x and y > 0: 
    print('Q1') 
if x < 0 and y > 0: 
    print('Q2') 
if x < 0 and y < 0: 
    print('Q3') 
if x > 0 and y < 0: 
    print('Q4') 
if x == 0 and y == 0: 
    print('Origem') 