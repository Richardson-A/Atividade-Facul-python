# Faça um programa para uma escola que tem 4 bimestres em cada
# bimestre o aluno terá uma prova e um trabalho, mostre a média de cada
# bimestre e ao final dos bimestres mostre se o aluno foi aprovado,
# reprovado ou em recuperação a nota deve ser 60 para aprovado, maior
# ou igual a 35 para recuperação e menor que 35 para reprovação.


prova_b1 = float(input('Digite a nota da Prova 1: '))
trabalho_b1 = float(input('Digite a nota da Trabalho 1: '))
prova_b2 = float(input('Digite a nota da Prova 2: '))
trabalho_b2 = float(input('Digite a nota da Trabalho 2: '))
prova_b3 = float(input('Digite a nota da Prova 3: '))
trabalho_b3 = float(input('Digite a nota da Trabalho 3: '))
prova_b4 = float(input('Digite a nota da Prova 4: '))
trabalho_b4 = float(input('Digite a nota da Trabalho 4: '))

resultado = prova_b1 + trabalho_b1 + prova_b2 + trabalho_b2 +prova_b3 + trabalho_b3 +prova_b4 + trabalho_b4

if(resultado >= 35 and resultado < 60):
    print('Prova especial, sua nota é:', resultado)
elif(resultado >= 60):
    print('Aprovado, sua nota é:', resultado)
else:
    print('Reprovado, não atingiu o mínimo de 35 pontos, sua nota é:', resultado)