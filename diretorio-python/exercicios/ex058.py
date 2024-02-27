from random import randint

num_pc = randint(0, 10)
num_user = 0
tentativa = 0
acertou = False
print('Adivinhe o número (0,10) escolhido pela maquina!')
while not acertou:

    num_user = int(input(f'tentativa {tentativa}: '))

    tentativa += 1

    if num_user == num_pc:

        acertou = True
    else:
        if num_user < num_pc:

            print('Seu chute foi menor')

        elif num_user > num_pc:

            print('Seu chute foi maior')


print(f'Você acertou em {
      tentativa} Tentativas! O Número escolhido era {num_pc}')
