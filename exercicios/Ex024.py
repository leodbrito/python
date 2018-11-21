# Ex024: Crie um programa que leia
# o nome de uma cidade e diga se ela
# começa ou não com o nome SÃO.

cidade = str(input('Digite o nome de uma cidade:')).strip()
print('são' in cidade.lower().split()[0])

# Resolução do Gustavo Guanabara:
print(cidade[:3].upper() == 'SÃO')