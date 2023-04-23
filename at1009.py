# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

nome = input('Nome do vendedor: ')
sal = float(input('Salário mensal do vendedor: '))
vend = float(input('Total de vendas em $: '))*0.15
tot = sal + vend

print('TOTAL = ', tot)