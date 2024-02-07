carteira = int(input('Quanto você tem na carteira? '))
dolar = 4.97
poder = carteira / dolar
print('Coma a cotação do dolar a {}, você pode comprar aproximadamente {:.0f} dolas'.format(dolar,poder))