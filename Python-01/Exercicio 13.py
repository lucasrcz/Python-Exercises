n1= float(input('Por favor, digite o seu salário atual:R$ '))
aumento= n1*0.15
salario= aumento + n1

print('O seu aumento irá ser de R${:.2f} e seu salário final ficará igual à R${:.2f}'.format(aumento,salario))