frase = str(input('Digite uma frase: ').strip())

print('A letra "a" aparece {} vezes nesta frase'.format(frase.upper().count('A')))
print('A letra "a" aparece pela primeira vez na posição {}'.format((frase.upper().find('A')+1)))
print('A letra "a" aparece pela última vez na posição {}'.format(frase.strip().upper().rfind('A')+1))
