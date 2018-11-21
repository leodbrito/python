# Ex010: crie um programa que leia
# quanto dinheiro uma pessoa tem
# na carteira e mostre quantos
# dolares ela pode comprar.
# Considere US$ 1 = R$ 3,93

r = float(input('Quantos Reais você tem na carteira? '))
d = r/3.93
print('Você pode comprar US${:.2f}'.format(d))