# ex009: Faça um programa que leia um
# úmero inteiro qualquer e mostre na
# tela sua tabuada.

n = int(input('Digite um numero inteiro: '))
print('Segue abaixo sua tabuada:\n\
        x  1 = {}\n\
        x  2 = {}\n\
        x  3 = {}\n\
        x  4 = {}\n\
        x  5 = {}\n\
        x  6 = {}\n\
        x  7 = {}\n\
        x  8 = {}\n\
        x  9 = {}\n\
        x 10 = {}'.format(n, n*2, n*3, n*4, n*5,
                          n*6, n*7, n*8, n*9, n*10))
