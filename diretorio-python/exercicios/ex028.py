import random

num_pc = random.randint(0,5)

num_user = int(input('Digite um numero entre 0-5: '))

if num_user == num_pc:
    print(f'Acertou!! o numero era {num_pc}')
else:
    print(f'Você errou, o numero era {num_pc}')