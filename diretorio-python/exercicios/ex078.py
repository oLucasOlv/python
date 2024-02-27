valores = []

for valor in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    maxValor = max(valores)
    minValor = min(valores)


print(valores)

print(f'O Valor maior é {maxValor} nas posições', end=' ')

for i,  v in enumerate(valores):

    if v == maxValor:

        print(f'{i + 1}...', end=' ')
print()
print(f'O valor menor é {minValor} nas posições', end=' ')
for i, v in enumerate(valores):

    if v == minValor:

        print(f'{i + 1}...', end=' ')
