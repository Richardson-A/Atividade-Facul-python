# Faça um programa para calcular o peso ideal, para pessoa levando
# em consideração a altura da pessoa. Para homens o calculo é
# (altura*72.7)-58 para mulheres (altura*62.1)-44.7

altura = float(input('Digite sua altura: '))
tipo = input('Digite M para mulher e H para homem: ').upper()

if(tipo == 'M'):
    result = (altura * 62.1) - 44.7
    print(f'Seu peso ideal é {result:.2f}')
elif(tipo == 'H'):
    result = (altura*72.7)-58
    print(f'Seu peso ideal é {result:.2f}')
else:
    print('Valor diferente de M ou H')

