t1 = int(input('Primeiro termo: '))
razao = int(input('Digite a Razão: '))

termo = t1
c = 1
final = 0
mais = 10

while mais != 0:
    final += mais
    while c <= final:
        print(f'{termo}', end=' - ')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('\nVocê quer mostrar mais alguns termos?\n'))
    
print(f'Progressão Finalizada com {final} termos mostrados.')


    # FORMA MAIS LONGA E MENOS SIMPLIFICADA
    # if c == final:
    #         '[S] Sim\n'
    #         '[N] Não\n'
    #         ).strip().upper()[0]

    #     if r == 'S':

    #         termoAdd = int(input('Quantos termos? '))

    #         final += termoAdd
    #         print(f'{termo}', end=' ')
    #         termo += razao
    #         c += 1
    #     else:
    #         print('cabou')
    #         final = 10
