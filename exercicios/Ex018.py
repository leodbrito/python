# Ex018: Faça um programa que
# leia um Ângulo qualquer e
# mostre na tela o valor do
# seno, cosseno e tangente
# desse ângulo.

import math
angulo = int(input('Digite o valor inteiro de um ângulo: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('\nAnalisando o ângulo de {}⁰...'.format(angulo))
print('O seno de {}⁰ é {}.'.format(angulo, seno))
print('O coseno de {}⁰ é {}.'.format(angulo, cosseno))
print('A tangente de {}⁰ é {}.'.format(angulo, tangente))
