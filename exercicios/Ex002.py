# Ex002: Crie um script Python que leia o dia,
# o mês e o ano de nascimento de uma pessoa e
# mostre uma mensagem com a data formatada.

dia = int(input('dia = '))
mes = str(input('Mes = ')).strip()
ano = int(input('Ano = '))
print('Você nasceu no dia {} de {} de {}.'.format(dia, mes, ano))