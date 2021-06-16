cidade = str(input('Digite o nome de uma cidade: '))
santos = cidade.upper().split()
s = 'SANTOS' in santos[0]

print('Existe SANTOS no primeiro nome da cidade? {}'.format(s))


print({s})