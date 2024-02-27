# valores = []
# valores.append(4)
# valores.append(2)
# valores.append(9)

# for chave, valor in enumerate(valores):
#     print(f'No index {chave} o valor é {valor}!')
# print('Chegou ao Fim!')

# valores = []

# for v in range(0, 5):

#     valores.append(int(input('Insira um valor: ')))

# print(f'Os valores digitados são: {valores}')

# FAZENDO COPIA DE LISTA

a = [2, 3, 4, 7]
b = a[:]
b[2] = 5
print(a)  # =>  [2, 3, 4, 7]
print(b)  # =>  [2, 3, 5, 7]

# Interligando Listas
# apartir que o uma lista recebe outra elas estão inteligadas
a = [2, 3, 4, 7]
b = a
b[2] = 5
print(a)  # =>  [2, 3, 5, 7]
print(b)  # =>  [2, 3, 5, 7]
