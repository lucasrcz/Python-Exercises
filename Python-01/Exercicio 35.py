a = float(input('Digite o valor de uma reta em M: '))
b = float(input('Digite outro valor de uma reta em M: '))
c = float(input('Digite mais um valor de uma reta em M: '))

if a - b < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('É possível formar um triângulo com essas retas!')
else:
    print('Não é possível formar um triângulo com essas retas!')