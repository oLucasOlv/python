r1 = int(input('Insira o primeiro valor: '))
r2 = int(input('Insira o segundo valor: '))
r3 = int(input('Insira o terceiro valor: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r3:
    if r1 == r2 and r2 == r3:
        print('Equilátero')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Escaleno')
    #elif r1 == r2 or r1 == r3 or r2 == r3:  opcional
    else:
        print('Isósceles')
else:
    print('Não é possivel formar um triangulo com esses valor')
