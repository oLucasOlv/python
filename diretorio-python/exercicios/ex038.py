n1 = int(input('Digite o primeiro Número: '))
n2 = int(input('Digite o segundo Número? '))

cores = {'azul': '\033[34m',
         'branco' : '\033[97m',
         'amarelo' : '\033[33m',
         'vazia' : '\033[m',
         'vermelho': '\033[31m'}

if n1 > n2:
    print(f'{cores["amarelo"]}O {n1} é o número maior{cores["vazia"]}')
elif n2 > n1:
    print(f'{cores["azul"]} O {n2} é o número maior {cores["vazia"]}')
else:
    print(f'{cores["vermelho"]}Não existe valor maior, os dois são iguais {cores["vazia"]}')
