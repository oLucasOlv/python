idade = int(input('Qual sua idade? '))

cores = {'vazia' : '\033[m',
         'verde': '\033[32m'}

if idade == 18:
    print(f'Você precisa se alistar ao {cores['verde']}serviço militar{cores['vazia']}')
elif idade < 18:
    print(f'Você ainda não precisa se alistar, apenas daqui a {18 - idade} anos')
elif idade > 18:
    print('Você já se alistou?\n 1 - sim \n 2 - não ')
    r = int(input(': '))
    if r == 1:
        print(f'Você não precisa se alistar! Já passou {idade - 18} ano do prazo de alistamento')
    else:
         print(f'Você precisa se alistar ao {cores['verde']}serviço militar{cores['vazia']}, o mais rapido possivel')