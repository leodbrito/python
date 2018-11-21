# Ex001: Crie um script Python que leia
# o nome de uma pessoa e mostre uma mensagem
# de boas-vindas de acordo com o valor digitado.

nome = str(input('Digite seu nome: ')).strip()
print('Olá {}, seja bem vindo!'.format(nome))