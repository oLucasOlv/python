vel_car = int(input('Qual a sua Velocidade? '))

multa = (vel_car - 80) * 7

if vel_car > 80:
    print(f'Você passou o Limite, sua multa é de R${multa:.2f}')
else:
    print('Você estar entre o limite')