""""
Crie um programa que leia um número inteiro qualquer e
mostre na tela se ele é par ou impar

"""

n = int(input('Digite um número: '))

par = n % 2

if par == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))