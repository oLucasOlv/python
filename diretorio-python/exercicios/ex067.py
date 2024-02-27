from random import randint, choice

num_user = int(input('Digite um número '))
user_choice = input('Impar ou Par? ').lower().strip()

choices = ['impar', 'par']
num_pc = 0
pc_choice = None
vitorias = derrotas = 0
res = 'S'


while True:
    num_pc = randint(0, 10)
    pc_choice = choice(choices)

    if pc_choice == user_choice:
        print(
            '\nVocês Empataram!!\n'
            f'Você escolheu {num_user} e {user_choice.capitalize()}\n'
            f'O PC escolheu {num_pc} e {pc_choice.capitalize()}')
        print(f'{num_pc + num_user} é Par' if (num_pc + num_user) %
              2 == 0 else f'{num_pc + num_user} é impar')

    elif (num_pc + num_user) % 2 == 0 and user_choice == choices[1]:
        print(
            '\nVocê ganhou!!\n'
            f'Você escolheu {num_user} e {user_choice.capitalize()}\n'
            f'O PC escolheu {num_pc} e {pc_choice.capitalize()}\n'
            f'{num_pc + num_user} é Par')
        vitorias += 1

    elif (num_pc + num_user) % 2 == 1 and user_choice == choices[0]:
        print(
            '\nVocê ganhou!!\n'
            f'Você escolheu {num_user} e {user_choice.capitalize()}\n'
            f'O PC escolheu {num_pc} e {pc_choice.capitalize()}\n'
            f'{num_pc + num_user} é Impar')
        vitorias += 1

    else:
        print(
            '\nVocê Perdeu!!\n'
            f'Você escolheu {num_user} e {user_choice.capitalize()}\n'
            f'O PC escolheu {num_pc} e {pc_choice.capitalize()}')
        print(f'{num_pc + num_user} é Par' if (num_pc + num_user) %
              2 == 0 else f'{num_pc + num_user} é impar')

        derrotas += 1

    print(f'\nVocê Ganhou {vitorias} vitorias e teve {derrotas} derrotas \n')

    res = input('jogar novamente? [S] [N] ').upper()[0]
    if res in 'Nn':
        print('O jogo Acabou!')
        break
    else:
        num_user = int(input('Digite um número '))
        user_choice = input('Impar ou Par? ').lower().strip()
