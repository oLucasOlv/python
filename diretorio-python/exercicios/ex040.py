n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2
print(f'Media : {media:.1f}')
if media < 5:
    print('\033[1;31m REPROVADO \033[m')
elif 7 > media >= 5: #and media <= 6.9:
    print('\033[1;33m RECULPERAÇÃO \033[m')
elif media >= 7:
    print('\033[1;32m APROVADO \033[m')