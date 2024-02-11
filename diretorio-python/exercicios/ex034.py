sal = float(input('Qual seu salário? '))

if sal >= 1250:
    print(f'Seu novo salário é de R${sal + (sal * 10 / 100):.2f}')
else:
    print(f'Seu novo salário é de R${sal + (sal * 15 / 100):.2f}')