# EX022: Crie um programa que leie
# o nome completo de uma pessoa e
# mostre:
# .O nome com todas as letras maiusculas e minusculas;
# .Quantas letras no total (sem considerar espaços);
# .Quantas letras tem o primeiro nome.

nome=str(input('Iforme seu nome completo: ')).strip()
print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome em letras maiusculas é: {}'.format(nome.lower()))
print('Seu nome possui {} letras!'.format(len(nome) - nome.count(' ')))
primeironome=nome.split()[0]
print('Seu primeiro nome é {} e possui {} letras!'.format(primeironome,len(primeironome)))