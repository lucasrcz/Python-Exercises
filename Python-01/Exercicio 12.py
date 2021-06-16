n1= float(input('Digite aqui o preço do produto que você deseja comprar nesta promoção: '))

desc=n1 * 0.05 

preçofinal= n1 - n1*0.05

print('O seu desconto é de 5%, equivalente à {:.2f}, sendo o preço final de {:.2f} ' .format(desc,preçofinal))