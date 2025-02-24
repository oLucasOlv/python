secret_word = "Carros".lower()
space = ['_']*len(secret_word)

abc = 'abcdefghijklmnopqrstuvwxyz'

max_error = 6
attempts = []

while max_error > 0 and "_" in space:

    print('Palavra: ' + ' '.join(space))
    print(f'Chances: {max_error}')
    print("Tentativas: " + ', '.join(attempts))
    player_letter = input("\nDigite Uma Letra: ").lower()

    if player_letter in attempts:
        print(f'A letra {player_letter} já foi digitada!')
        continue
    if player_letter not in abc:
        print('Caractere invalido')
        continue

    attempts.append(player_letter)

    if player_letter in secret_word:
        for i, l in enumerate(secret_word):
            if l == player_letter:
                space[i] = l
    else:
        max_error -= 1
        print(f"A letra '{player_letter}' não estar na palavra!")

if "_" not in space:
    print(f'Você Acertou! A palavra era {secret_word}')

else:
    print(f'Você perdeu! A palavra era {secret_word}')
