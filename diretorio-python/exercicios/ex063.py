# n1 = int(input('Insira um número: '))

# c = 1
# a, b = 0, 1 # criando variaveis

# while c <= n1:
#     print(a, end=' ')
#     a, b = b, a + b
#     # atualização simultâne de variavel
#     # a recebe o valor de b, depois é somado com o valor de b.
#     # 0, 1 = 1, 1 + 1
#     #atualizada ficara > 1, 2
#     c += 1


n1 = int(input('Insira um número: '))

c = 3
t1 = 0
t2 = 1
print(f'{t1} {t2}', end=' ')
while c <= n1:
    t3 = t1 + t2
    print(f'{t3}', end=' ')
    t1 = t2
    t2 = t3
    c += 1
