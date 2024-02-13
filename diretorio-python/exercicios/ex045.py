from random import randint
from time import sleep


"""
Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).

"""


itens = {'1' : 'Pedra',
        '2' : 'Tesoura',
        '3' : 'Papel'}



print('\nEscolha:\n'
      '1 - Pedra\n'
      '2 - Tesoura\n'
      '3 - Papel\n')

choice_pc = randint(1,3)

choice_user = int(input('Qual sua jogada? '))
if choice_user > 3:
    print('Tentativa invalida, tente de 1 - 3')
else:
    
    print('JO')
    sleep(1.3)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(0.3)

    print('-=' * 14)
    print(f'Você Jogou {itens[f'{choice_user}']}\n'
        f'Computador Jogou {itens[f'{choice_pc}']}')
    print('-=' * 14)

    if choice_user > 0 and choice_user <= 3 :
        if choice_user == choice_pc:
            print('Empate')

        elif choice_user == 1 and choice_pc == 2 or choice_user == 2 and choice_pc == 3 or  choice_user == 3 and choice_pc == 1:
            print('Você ganhou')

        else: 
            print('Perdeu')

