preco = float(input('Qual o preço? R$:'))
n_preco = preco - (preco * 5 / 100)
print('De ${:.2f} para ${:.2f} com 5% de desconto'.format(preco,n_preco))