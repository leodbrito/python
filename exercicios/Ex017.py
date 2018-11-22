# Ex017: Faça um programa que leia o
# comprimento do cateto oposto e do
# cateto adjacente de um triangulo
# retangulo, calcule e mostre o
# comprimento da Hipotenusa.
import math
cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digitw o comprimento do cateto adjacente: '))

# Utilizando o conceito hipotenusa
# ao quadrado é igual a soma
# do quadrado dos catetos.
hipotenusa1 = math.sqrt(cato**2+cata**2)

# utilizando diretamente o metodo hypot do módulo math
hipotenusa2 = math.hypot(cato, cata)

print('\nO comprimento da hipotenusa é {}.'.format(hipotenusa2))
