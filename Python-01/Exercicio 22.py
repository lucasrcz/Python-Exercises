"""
Crie um programa que leia o nome completo de uma pessoa
e mostre:
-o nome com todas as letras maiúsculas
-o nome com todas as letras minúsculas
-Quantas letras ao todo(sem considerar o espaço)
-Quantas letras tem o primeiro nome
"""

nome = str(input('Digite seu nome completo:'))

print('Seu nome em maiúsculo fica da seguinte forma: {}'.format(nome.strip().upper()))
print('Seu nome em maiúsculo fica da seguinte forma: {}'.format(nome.strip().lower()))
print('Seu nome completo tem {} carácteres'.format(len(nome) - nome.count(' ')))
divido = nome.split()
print('Seu primeiro nome tem {} carácteres'.format(len(divido[0])))

