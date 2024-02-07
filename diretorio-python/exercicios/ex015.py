km = float(input('Quantos KM rodado? '))
dia = int(input('Quantos Dias foi alugado? '))

custo_total =  (dia * 60) + (km * 0.15)  

print('O Total a se pagar pelo aluguel do carro é de R${:.2f}'.format(custo_total))