"""
Faça um programa que leia um número na tela cada um dos digitos separados

ex: Digite um número:1834

unidade:4
Dezena:3
Centena:8
milhar:1
"""

num = str(input('Digite um número entre 0 e 9999'))

numt = num.strip()

print('A Unidade desse número é {}'.format(numt[3]))
print('A Dezena desse número é {}'.format((numt[2])))
print('A Centena desse número é {}'.format((numt[1])))
print('O Milhar desse número é {}'.format((numt[0])))

