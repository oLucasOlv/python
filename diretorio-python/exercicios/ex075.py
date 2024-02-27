n1 = int(input('Digite o primerio valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))

tupla = (n1, n2, n3, n4)

print(tupla)
print(f'O 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O Valor 3 esta na {tupla.index(3)+1} posição')
else:
    print(f'O Valor 3 não foi digitado')

print(f'Os números pares são ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')

