lista = []
r = 'S'

while r == 'S':
    num = int(input('Digite um número: '))

    if num in lista:
        print('Esse Valor já estar na lista!')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    r = input('Deseja continuar? [S]|[N] ').upper().strip()[0]



lista.sort()
print('')
print('ITENS DA LISTA')
for item in lista:
    print(item, end=' ')
