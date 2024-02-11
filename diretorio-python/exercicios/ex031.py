dis_viagem = int(input('Qual a distancia da viagem? '))

pas200 = dis_viagem * 0.50
paslonga = dis_viagem * 0.45

if dis_viagem <= 200:
    print(f'Sua passagem é de R${pas200:.2f}')
else:
    print(f'Sua Passagem é de R${paslonga:.2f}')