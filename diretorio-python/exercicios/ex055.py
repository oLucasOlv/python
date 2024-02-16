
maior_peso = 0
menor_peso = 0

for p in range(1,6):
    peso = float(input('Qual seu peso? '))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print(maior_peso, menor_peso)