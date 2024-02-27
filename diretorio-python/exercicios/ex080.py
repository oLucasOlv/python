
lista = []

for c in range(0, 5):

    num = int(input('Digite Um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista): 
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1


# 2 7
print(lista)
