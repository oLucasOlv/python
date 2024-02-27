lista = []
r = 'S'


c = 0
    #n = int(input('Digite um número: '))
while r == 'S':
    lista.append(int(input('Digite um número: ')))
    c += 1
    r = input('Deseja continuar? [S]|[N] ').upper().strip()[0]

lista.sort(reverse=True)
print()
print(f'{c} números foram digitados')
print()
print(f'Lista na ordem decrescente: {lista}')
print()
if 5 in lista:
    print('O 5 esta na lista!')
else:
    print('O 5 não esta na lista!')