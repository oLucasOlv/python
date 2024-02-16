num = int(input('Digite um numero: '))

vezes_div = 0

for c in range(1, num + 1):

    if num % c == 0:
        print('\033[33m', end=' ')
        vezes_div += 1
    else:
        print('\033[31m', end=' ')

    print(f'{c}''\033[m', end=' ')

print(f'\nNúmero {c} foi divisivel {vezes_div} vezes')

if vezes_div == 2:
    print('E por isso ele é Primo!')
else:
    print(f'E por isso ele Não é Primo! ')
