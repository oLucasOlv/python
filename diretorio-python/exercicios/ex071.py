print('=' * 30)
print(f'{'BANCO':^30}')
print('=' * 30)
saque = int(input('QUANTO VOCÊ DESEJA SACAR? R$'))

total = saque
nota = 50
totalNotas = 0

while True:
    if total >= nota:
        total -= nota
        totalNotas += 1
    else:
        if totalNotas > 0:
            print(f'Total de {totalNotas} notas de {nota}')
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1

        totalNotas = 0

        if total == 0:
            break

# MODO ANTES DE VER O EXERCICIO

# notas50 = saque // 50
# saque = saque - notas50 * 50
# notas20 = saque // 20
# saque = saque - notas20 * 20
# notas10 = saque // 10
# saque = saque - notas10 * 10
# notas1 = saque // 1

# print(f"""
# TOTAL de {notas50} notas 50
# TOTAL de {notas20} notas 20
# TOTAL de {notas10} notas 10
# TOTAL de {notas1} notas 1
# """)
