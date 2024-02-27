
somar = 1
multi = 2
maior = 3
novos_num = 4
sair = 5
escolha = 0

v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))
while escolha != 5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
          
          """)
    escolha = int(input('Qual sua Opção?\n'))
    if escolha != 5:
        if escolha == 1:
            somar = v1 + v2
            print(f'O valor da soma é: {somar}')
            print('-='*15)
            
        elif escolha == 2:
            multi = v1*v2
            print(f'O valor da multiplicação é: {multi}')
            print('-='*15)
        elif escolha == 3:
            if v1 > v2:
                print(f'O numero maior é {v1}')
                print('-='*15)
            elif v1 == v2:
                print('os dois números são so mesmos')
                print('-='*15)
            else:
                print(f'O numero maior é {v2}')
                print('-='*15)
        elif escolha == 4:
            print('Escolha novos Números: ')
            v1 = int(input('Valor 1: '))
            v2 = int(input('Valor 2: '))
            print('-='*15)
        else:
            print('Escolha Invalida')
            print('-='*15)
