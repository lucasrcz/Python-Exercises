salario = float(input('Digite o valor do seu salário: '))

s1= salario * 0.1

s2= salario * 0.15

#aumento1= s1 + salario
#aumento2= s2 + salario

if salario>1250.00:
    print('Seu aumento salárioal será de R${} somando um total de R${}'.format(s1, salario+s1))
else:
    print('Seu aumento salárial será de R${} somando um total de R${}'.format(s2, salario+s2))