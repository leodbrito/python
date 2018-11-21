frase='Estou aprendendo Python'

print(frase)
print
frase2=frase.split()[0]+' '+frase.split()[1]
buscapython=frase.lower().find('python')
curso1='python'
curso2='java'
print(buscapython)

print(frase2 ,frase.split()[2].lower().replace('python',frase.split()[1].capitalize()))

frase3=frase.split()[:3]

print(frase3)

print('-'.join(frase))
print(' '.join(frase3))

print(int(frase.count('')))
print(int(frase.count(' ')))

print(int(frase.count(''))-int(frase.count(' ')))

print()




