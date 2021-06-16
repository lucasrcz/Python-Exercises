medida=float(input('Digite uma médida em metros que você deseja converter: '))

cm= medida * 100
mm= medida * 1000

print('A sua medida convertida para centímetros é igual a {:.2f} e para milímetros é igual a {:.2f}' .format(cm,mm))