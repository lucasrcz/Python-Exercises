# O mesmo professor do desafio anterior quer sortear a ordem
#de apresentação do trabalho dos alunos. Faça um programa que
#leia o nome dos quatro alunos e mostre a ordem sorteada

import random
from random import shuffle

print('Bem vindo ao gerador de Listas Randômicas 1.0.')

a1 = str(input('Digite o nome do segundo Aluno: '))
a2 = str(input('Digite o nome do segundo Aluno: '))
a3 = str(input('Digite o nome do terceiro Aluno: '))
a4 = str(input('Digite o nome do quarto Aluno: '))
lista=[a1,a2,a3,a4]
random.shuffle(lista)

#Cria-se a lista e logo após embaralha a mesma para que a lista saia de forma aleatória no print

print('A ordem da lista gerada randômicamente é a seguinte: {}'.format(lista))

#Se você para selecionar