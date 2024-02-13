num = int(input('Digite um número inteiro: '))


cores = {'azul': '\033[34m',
         'branco' : '\033[97m',
         'amarelo' : '\033[33m',
         'vazia' : '\033[m',
         'vermelho': '\033[31m',
         'verde' : '\033[32m'}

print(f'{cores["azul"]} Escolha uma Opção {cores['vazia']}')

print('{0}-{1} {2}1{1} Para {0}Binário{1}\n'
      '{0}-{1} {2}2{1} Para {0}Octal{1}\n'
      '{0}-{1} {2}3{1} Para {0}Hexadecimal{1}\n'.format(cores['amarelo'], cores['vazia'], cores['azul']))

e = int(input(': '))

if e == 1:
    print(f'O binário de {num} é {cores['verde']} {bin(num)[2:]} {cores['vazia']}')
elif e == 2:
    print(f'O octal de {num} é {cores['verde']} {oct(num)[2:]} {cores['vazia']}')
elif e == 3:
    print(f'O hexadecimal de {num} é {cores['verde']} {hex(num)[2:]} {cores['vazia']}')
else:
    print(f'{cores["vermelho"]} ERROR OPÇÃO INVALIDA {cores['vazia']}')