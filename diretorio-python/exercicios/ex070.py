produto = input('Nome do Produto: ')
preco = float(input('Preço Do Produto: R$'))

total_gasto = pdt1000 = produtos = precoPdt =  0 
pdtBarato = ''
r = 'S'
while True:
    produtos += 1
    if produtos == 1:
        pdtBarato = produto
        precoPdt = preco
    elif preco < precoPdt:
        pdtBarato = produto
        precoPdt = preco

    if preco > 1000:
        pdt1000 += 1

    total_gasto += preco
    r = input('Deseja Continuar? ').upper().strip()[0]
    while r not in 'SN':
        r = input('Deseja Continuar? ').upper().strip()[0]
    if r == 'N':

        print(f"""
Você comprou {produtos} Produtos
O total da sua compra foi {total_gasto:.2f}
Temos {pdt1000} produtos custando mais de R$1000.00
O produto mais barato foi {pdtBarato.capitalize()} que Custou R${precoPdt:.2f} """)
        break
    else:
        produto = input('Nome do Produto: ')
        preco = float(input('Preço Do Produto: R$'))  
