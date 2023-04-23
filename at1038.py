# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

print('Bem vindo!\nSegue as opções de lanches abaixo:  \n\n1- Cachorro quente: R$ 4,00 \n2- X-Salada: R$ 4,50 \n3- X-Bacon: R$ 5,00 \n4- Torrada: R$ 2,00 \n5- Refrigerante: R$ 1,50') 
pedido = input('\nQual desses você deseja? Insira o número do alimento para prosseguir: ') 
preco = 0 
 
while True: 
    if pedido == '1': 
        preco += 4.00 
    elif pedido == '2': 
        preco += 4.50 
    elif pedido == '3': 
        preco += 5.00 
    elif pedido == '4': 
        preco += 2.00 
    elif pedido == '5': 
        preco += 1.50 
    condicao = input('\nDeseja pedir algo a mais? Se sim, digite "s" se não digite "n": ') 
    if condicao == 's': 
        pedido = input('\nO que seria?: \n\n1- Cachorro quente: 4,00 \n2- X-Salada: 4,50 \n3- X-Bacon: 5,00 \n4- Torrada: 2,00 \n5- Refrigerante: 1,50\n\nInsira novamente: ') 
        if pedido < '6': 
            print('Registrado!') 
        elif pedido > '5': 
            print('Ops! não entendemos.') 
    if condicao == 'n': 
        break 
 
print(f'\nO valor total foi: R$ {preco}') 