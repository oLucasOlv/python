#programa para ler um preço e calcular o desconto a vista e o aumento parcelado 
preco = float(input('Qual o preço do produto? R$:'))
desconto = preco - (preco*10/100)
aumento_parcelado = preco + (preco *  8 / 100)

print('Preço caso você pague a vista: R${:.2f}, Preço caso você queira parcelar: R${:.2f}' .format(desconto, aumento_parcelado))