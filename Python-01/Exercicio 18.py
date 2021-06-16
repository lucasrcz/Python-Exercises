from math import cos, tan, sin, degrees, radians

angulo = float(input('Digite um ângulo: '))

cosn = cos(radians(angulo))
sinn = sin(radians(angulo))
tann = tan(radians(angulo))


print('O seu coseno do ângulo é igual à {:.2f}, o seno é {:.2f} e a tangente é {:.2f} em radianos'.format(cosn, sinn, tann))
