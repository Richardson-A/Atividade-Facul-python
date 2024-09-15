# Faça um programa para uma loja virtual calcular a compra dos produtos
# e mostrar ao final o valor total da compra, o valor a vista com desconto
# de 10%, e o valor com acréscimo de 5% em compra parcelada de 3x e
# mostre também o valor da parcela. Os produtos são, Iphone, Samsung
# s24, tablet, ipad e notebook

iphone = 2500.00
s24 = 1380.25
tablet = 500.00
ipad = 1650.00
notebook = 1299.99

total = iphone + s24 + tablet + ipad +notebook
t_desconto = total * 0.9 #(total/100)*90
parcela = (total * 1.05) / 3

print("O valor total da compra é: R$", total)
print("O valor total da compra com desconto a vista é: R$", t_desconto)
print("O valor da parcela com 5% de juros é: R$", parcela)
