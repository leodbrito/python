# Ex025: Crie um programa que leia
# o nome de uma pessoa e diga se
# ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome possui Silva é {}'.format('silva' in nome.lower()))
