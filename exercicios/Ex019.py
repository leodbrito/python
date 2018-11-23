# Ex019: Um professor quer
# sortear um dos seus quatro
# alunos para apagar o quadro.
# Faça um programa que ajude
# ele lendo o nome deles e
# escrevendo o nome do escolhido.

import random

aluno1 = str(input('Informe o nome do priemiro aluno: ')).strip()
aluno2 = str(input('Informe o nome do segundo aluno: ')).strip()
aluno3 = str(input('Informe o nome do terceiro aluno: ')).strip()
aluno4 = str(input('Informe o nome do quarto aluno: ')).strip()
alunos = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(alunos)
i = random.randint(0, 3)
print('O aluno escolhido para apagar o quadro foi: {}.'.format(escolhido))
