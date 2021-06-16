from math import hypot

oposto = float(input('Digite o comprimento do cateto oposto em M: '))
adj = float(input('Digite o comprimento do cateto adjacente em M: '))

print('O comprimento da hipotenusa é igual á {:.2f} M '.format(hypot(oposto, adj)))
