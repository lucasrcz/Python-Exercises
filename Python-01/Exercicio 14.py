C= float(input('Digite a temperatua atual para que seja feita a conversão em Fahrenheit: '))
F= float(C * 1.8 + 32)
FC=float((F-32.0))/ 1.8

print('A temperatura atual {:.2f}Cº é igual a {:.2f}Fº'.format(C,F))