n = soma = 0
while True:       # LOOP INFINITO
    n = int(input('Digite um número: '))
    if n == 999:
        break     # INTEROMPENDO O LOOP
    soma += n
print(f'A soma vale {soma}')
