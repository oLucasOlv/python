import random

"""
Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).


"""


itens = {'1' : 'pedra',
         '2' : 'tesoura',
         '3' : 'Papel'}

print('\nEscolha:\n'
      '1 - Pedra\n'
      '2 - Tesoura\n'
      '3 - Papel\n')
choice_user = int(input(': '))
choice_pc = random.randint(1,3)

if choice_user > 0 and choice_user <= 3 :
    if choice_user == choice_pc:
        print('Empate')
        print(f'Você escolheu {itens[f'{choice_user}']} e a maquina escolheu {itens[f'{choice_pc}']}')

    elif choice_user == 1 and choice_pc == 2 or choice_user == 2 and choice_pc == 3 or  choice_user == 3 and choice_pc == 1:
        print('Você ganhou')

        print(f'Você escolheu {itens[f'{choice_user}']} e a maquina escolheu {itens[f'{choice_pc}']}')

    
    else: 
        print('Perdeu')
        print(f'Você escolheu {itens[f'{choice_user}']} e a maquina escolheu {itens[f'{choice_pc}']}')
else:
    print('Tentativa invalida, tente de 1 - 3')
    

