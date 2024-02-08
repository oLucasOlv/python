from math import hypot, floor

co = int(input('Valor do cateto oposto: '))
ca = int(input('Valor do cateto adjacente: '))

h = hypot(co,ca)

print(f'O valor da hipotenusa é de {floor(h)}')