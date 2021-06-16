from random import randint

print('Bem vindo ao jogo de adivinhação')

n = int(input('Digite um número de 0 a 5: '))

m = randint(0, 5)

if m == n:
    print('Você adivinhou o número, parabéns!')
else:
    print('Você perdeu :(, tente novamente')
    
