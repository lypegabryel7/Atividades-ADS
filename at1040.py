# Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

n1 = int(input('Insira a 1º nota: '))*0.20 
n2 = int(input('Insira a 2º nota: '))*0.30 
n3 = int(input('Insira a 3º nota: '))*0.40
n4 = int(input('Insira a 4º nota: '))*0.10 
media = (n1 + n2 + n3 + n4) 
if media >= 7.00: 
    print(f'Media: {media}, aluno aprovado') 
elif media < 7.00 and  media >= 5.00: 
    print('Aluno nos exames finais.') 
    med_final = int(input('Insira a nota final: ')) 
    med_final = (med_final + media) / 2 
    if med_final < 5: 
        print(f'Nota final: {med_final}\n Aluno reprovado.') 
    elif med_final >= 5: 
        print(f'Nota final: {med_final}\n Aluno aprovado.') 
elif media < 5: 
    print(f'Média: {media}\n Aluno reprovado.')