l=float(input('Digite aqui a largura da parede em metros, que você deseja pintar: '))
alt=float(input('Digite aqui a altura da parede em metros, que você deseja pintar: '))
m2= l*alt
tinta= m2 / 2
print('A área da parede que você deseja pintar equivale a {} m², sendo assim você irá precisar de {} litros de tinta para pinta-la' .format(m2,tinta))