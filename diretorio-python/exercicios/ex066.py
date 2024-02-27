n = int(input('Digite um número '))
soma = 0
c = 1

while True:
    n = int(input('Digite um número '))
    if n == 999:
        break
    soma += n
    c += 1
print(f'Foram digitados {c} números e a soma entre eles é de {soma}')