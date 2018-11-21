# Ex012: faça um algoritmo que leia
# o preço de um produto e mostre seu
# novo preço, com 5% de desconto.

p = float(input('Digite o preço de um produto: '))
print('Este produto custará R${:.2f} com 5% de desconto!'.format(p-p*0.05))
