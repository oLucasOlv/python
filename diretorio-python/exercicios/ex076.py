
print('=' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('=' * 50)

lista = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
         'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
c = 0
soma = 0
p = 0
for item in range(0, len(lista)):
    #if c < len(lista):
    if item %2 == 0:
        print(f'{lista[item]:.<35}.R${lista[item+1]:>10.2f}')
    else:
 #   c += 2
#    if (c-1) % 2 == 1:
        p = lista[item]
        soma += p

print('=' * 50)
print(f'{'Valor total':.<35}.R${soma:>10.2f}')
print('=' * 50)
