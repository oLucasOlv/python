n1 = int(input('Digite o primeiro Número: '))
n2 = int(input('Digite o segundo Número: '))
n3 = int(input('Digite o terceiro Número: '))

if n1 > n2 and n1> n3:
    print(f'{n1} é maior')
elif n2>n3:
    print(f'{n2} é maior')
else:
    print(f'{n3} é maior')