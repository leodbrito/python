# Ex004: Faça um programa que leia algo pelo
# teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

v = input('Digite algo: ')
print('\nqual o tipo primitivo? {} \n\
é numérico? {} \n\
é somente caracter? {} \n\
é alfanumérico? {} \n\
é somente espaço vazio? {} \n\
está todo em maiúsculo? {} \n\
está todo em minúsculo? {}'.format(type(v),
                                   v.isnumeric(),
                                   v.isalpha(),
                                   v.isalnum(),
                                   v.isspace(),
                                   v.isupper(),
                                   v.islower()))
