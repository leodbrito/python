# Ex011: Faça um programa que leia
# a largura e a altura de uma parede
# em metros, calcule sua área e a
# quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de
# tinta, pinta uma área de 2m².

b = float(input('Digite a largura de sua parede em metros: '))
h = float(input('Digite a altura de sua parede em metros: '))
a = b*h
t = a/2
print('\nSua parede tem uma área de {}m² e precisa de {} litros de tinta para ser pintada!'.format(a, int(t)))
