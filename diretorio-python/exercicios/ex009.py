n = int(input('Digite um número: '))


print('-'*12)
for produto in range(0,14) : 
    m = n * produto
    print('{} x {} = {}'.format(n,produto,m))
print('-'*12)