# Faça um programa para definir em uma condicional se um número é
# maior que 5, menor que 5 ou igual a 5.
import random

numero = int(input('Digite um número: '))
adivinha = random.randrange(0, 10)

if(numero > adivinha):
    print('Numero é maior que o secreto, o Numero digitado é:', numero)
elif(numero < adivinha):
    print('Numero é menor que o secreto o Numero digitado é:', numero)
else:
    print('Numero é igual ao secreto o Numero digitado é:', numero)

