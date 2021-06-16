print('Bem vindo ao terminal de atendimento automático para compra de passagens de ônibus!')
km = float(input('Digite quantos kilometros a sua viagem tem: '))

km1 = 0.50 * km

km2 = 0.45 * km

if km<= 200:
    print('O valor da sua passagem é igual a {}'.format(km1))
else:
    print('O Valor da sua passagem é igual a {}'.format(km2))

print('Boa viagem!')
