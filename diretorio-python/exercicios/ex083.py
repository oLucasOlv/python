lista = []

exp = input('Digite uma expressão: ')
lista.append(exp)
# numeros de parentes não pode ser impar
paren = 0

for c in lista[0]:
   
    if c in '()':
        paren += 1

if paren % 2 == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão não é valida')


