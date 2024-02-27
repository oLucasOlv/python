numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze","Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")


while True:
    num_user = int(input('Digite um número entre 0 e 20: '))
    if num_user >= 0 and num_user <= 20:
        break
    print('Tentativa Invalida')
print(f'Você digitou o numero {numeros[num_user]}')
