from math import factorial

print('Achar o Fatorial De um Nùmero')

n = int(input('Digite um número: '))
c = n
f = 1

#Fatorial com WHILE

while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)


# Fatorial com FOR
# for c in range(n, 0, -1):
#     print(f'{c}', end=' ')
#     print('x'if c > 1 else '=', end=' ')
#     f *= c
# print(f)

# Achar Fatorial com Modulo MATH
# print(f'Fatorial de {n} = {factorial(n)}')
