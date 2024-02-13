peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc =   peso / altura**2

print(f'{imc:.2f}')
if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 30:
    print('Obesidade')
elif imc >40:
    print('Obesidade Mórbida')