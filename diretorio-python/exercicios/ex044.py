preco = float(input('Qual o preço do produto? '))

cores = {'azul': '\033[34m',
         'branco' : '\033[97m',
         'amarelo' : '\033[33m',
         'vazia' : '\033[m',
         'vermelho': '\033[31m',
         'verde':'\033[32m'}


preco_vista = preco - (preco * 10 / 100)
preco_vista_cartao =  preco - (preco * 5 / 100)
cartao2x = preco
print('Qual opção para pagar?')

print('\n1 - à vista dinheiro/cheque 10% de desconto: \n'
      '2 - à vista no cartão 5% de desconto\n'
      '3 - 2x no cartão, preço normal\n'
      '4 - 3x ou mais no cartão, 20% de juros\n')

r = int(input(': '))
if r == 1:
     print(f'Preço Final: {cores['verde']}R${preco_vista:.2f}{cores["vazia"]}')
elif r== 2:
     print(f'Preço Final: {cores['verde']}R${preco_vista_cartao:.2f}{cores["vazia"]}')
elif r == 3:
    print(f'Preço Final: {cores['verde']}R${preco:.2f}{cores["vazia"]}')
elif r == 4:
    parcelas = int(input('Quantas parcelas você quer? 3 - 12: '))
    if parcelas >= 3 and parcelas<= 12:
        cartao3x = preco * (1 + 20 / 100) ** parcelas
        print(f'Preço Final: {cores['verde']}R${cartao3x:.2f}{cores ["vazia"]}')
    else:
        input(f'{cores['vermelho']} ERRO: NUMERO DE PARCELAS MAIOR DO QUE O PERMITIDO {cores["vazia"]}')
else:
    print(f'{cores["vermelho"]}ERRO: RESPOSTA INVALIDA{cores["vazia"]}')

    