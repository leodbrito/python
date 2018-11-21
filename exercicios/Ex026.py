# Ex026: Faça um programa que leia
# uma frase pelo teclado e mostre:
# .Quantas vezes aparece a letra "A";
# .Em que posição ela aparece a primeira vez;
# .Em que posição ela apareca a última vez.

frase = str(input('Digite uma frase:')).strip()
print('A letra "A" aparece {} vezes na sua frase.'.format(frase.lower().count('a')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.lower().find('a')+1))
print('A letra "A" aparece pela ultima vez na posição {}'.format(frase.lower().rfind('a')+1))