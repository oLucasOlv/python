c = media = soma = maior = menor = 0

res = 'S'

while res not in 'N':
    c += 1
    n = int(input('Digite um número: '))
    soma += n

    res = input('Deseja Continuar? [S] Sim [N] Não : ').strip().upper()[0]

    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / c
print(f'\nMedia: {media}\n' f'Maior Nùmero: {maior}\n' f'Menor Número: {menor}')
