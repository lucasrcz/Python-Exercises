""""
escreva um programa que leia a velocidade de um carro
se ele ultrapassar 80 km/h mostre uma msg dizendo que ele foi multado
a multa vai custar R$ 7.00 por cada KM acima do limite
"""

vel = float(input('Digite a velocidade atual do seu carro: '))
multa = (vel - 80) * 7.0
if vel > 80.0:
    print('Você foi multado, sua multa está no valor de {}'.format(multa))
else:
    print('Você está dentro da velocidade permitida :)')