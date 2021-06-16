ano = int(input('Digite o ano para saber se ele é bisexto ou não: '))

if ano % 4 ==0 and ano % 100 != 0 or ano % 4==0 and ano % 100 ==0 and ano % 400 ==0:
    print('{} é um ano bisexto!'.format(ano))
else:
    print('{} não é um ano bisexto!'.format(ano))
