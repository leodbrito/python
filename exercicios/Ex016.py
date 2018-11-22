# Ex016: Crie um programa que leia um
# número REAL qualquer pelo teclado e
# e mostre na tela a sua porção inteira.
# Ex:
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

import math
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n, math.trunc(n)))
