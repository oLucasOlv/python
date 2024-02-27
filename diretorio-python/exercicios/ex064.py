
c = soma = 0 

num_user = int(input('DIgite um numero: '))
while num_user != 999:

    soma += num_user
    c += 1
    num_user = int(input('DIgite um numero: '))

print(f'Você digitou {c}, e a soma entre eles foi de {soma}')
