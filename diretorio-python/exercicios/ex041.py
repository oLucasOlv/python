from datetime import date
ano_atual = date.today().year

ano_user = int(input('Ano Nascmento? '))
idade = ano_atual -ano_user

cores = {'azul': '\033[34m',
         'branco' : '\033[97m',
         'amarelo' : '\033[33m',
         'vazia' : '\033[m',
         'vermelho': '\033[31m'}

if idade <= 9:
    print(f'Com {cores["amarelo"]} {idade} anos {cores["vazia"]} você é {cores["azul"]} MIRIM {cores["vazia"]}')
elif idade <= 14:
    print(f'Com {cores["amarelo"]} {idade} anos {cores["vazia"]} você é {cores["azul"]} INFANTIL {cores["vazia"]}')
elif idade <= 19:
    print(f'Com {cores["amarelo"]} {idade} anos {cores["vazia"]} você é {cores["azul"]} JUNIOR {cores["vazia"]}')
elif idade == 20:
    print(f'Com {cores["amarelo"]} {idade} anos {cores["vazia"]} você é {cores["azul"]} SÊNIOR {cores["vazia"]}')
else:    
    print(f'Com {cores["amarelo"]} {idade} anos {cores["vazia"]} você é {cores["azul"]} MASTER {cores["vazia"]}')