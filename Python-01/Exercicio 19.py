#um professor quer sortear um dos quatro alunos
#para apagar o quadro. faça um programa que ajude
#ele, lendo o nome deles e escrevendo o nome do escolhido

import random
print('Bem vindo ao sorteador de Apagadores de Quadro 1.0 Alpha')
a1 = str(input('Digite o nome do(a) primeiro(a) Aluno(a): '))
a2 = str(input('Digite o nome do(a) segundo(a) Aluno(a): '))
a3 = str(input('Digite o nome do(a) terceiro(a) Aluno(a): '))
a4 = str(input('Digite o nome do(a) quarto(a) Aluno(a): '))

lista=[a1,a2,a3,a4]

print('A lista dos sorteados é a seguinte {}'.format(lista))

print('O sorteado da lista é o(a) aluno(a): {}' .format(random.choice(lista)))

#Criamos uma lista para ser sorteado dentro do comando random.choice
#que seleciona de forma aleatória um elemento da lista que criamos.
