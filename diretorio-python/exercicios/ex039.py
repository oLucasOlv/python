from datetime import date

ano_atual = date.today().year
sexo_user = input('Qual seu sexo? ' )
ano_user = int(input('Que ano você nasceu? '))
idade =  ano_atual - ano_user

cores = {'vazia' : '\033[m',
         'verde': '\033[32m'}
if sexo_user.lower() != 'feminino':
    if idade == 18:

        print(f'Você precisa se alistar ao {cores['verde']}serviço militar{cores['vazia']}')

    elif idade < 18:

        print(f'Você ainda não precisa se alistar, apenas daqui a {18 - idade} anos')
        print(f'Seu alistamento sera em {ano_atual + (18-idade)}')
    elif idade > 18:

        print('Você já se alistou?\n 1 - sim \n 2 - não ')
        r = int(input(': '))

        if r == 1:

            print(f'Você não precisa se alistar! Já passou {idade - 18} ano do prazo de alistamento')

        else:

            print(f'Você precisa se alistar ao {cores['verde']}serviço militar{cores['vazia']}, o mais rapido possivel')

            print(f'Seu alistamento seria em {ano_atual - (idade - 18) }')  
    else:
        print('error ao responder')
else:
    print('No Brasil o alistamento militar obrigatorio é somente para homens!')    