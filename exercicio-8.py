# Faça um programa para calcular as notas de um aluno, onde ele recebera
# o valor da A1, A2 e A3 fará o calculo para dizer se foi aprovado, reprovado
# ou prova especial. Aprovado maior ou igual a 70, prova especial maior ou
# igual a 40, reprovado menor que 40.

a1 = float(input('Digite a nota da A1: '))
a2 = float(input('Digite a nota da A2: '))
a3 = float(input('Digite a nota da A3: '))

resultado = a1+a2+a3

if(resultado >= 40 and resultado < 70):
    print('Prova especial, sua nota é:', resultado)
elif(resultado >= 70):
    print('Aprovado, sua nota é:', resultado)
else:
    print('Reprovado, não atingiu o mínimo de 40 pontos, sua nota é:', resultado)