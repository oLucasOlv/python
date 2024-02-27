lista = []
listaImpar = []
listaPar = []
r = 'S'
while r == 'S':
    lista.append(int(input('Digite um número: ')))
    r = input('Deseja continuar? [S] [N] ').upper().strip()[0]

for c in lista:
    if c % 2 == 0:
        listaPar.append(c)
    elif c % 2 == 1:
        listaImpar.append(c)
   
       
   


print()
print(lista)
print(listaPar)
print(listaImpar)
