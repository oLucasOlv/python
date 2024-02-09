nome = input('Qual Seu nome completo? ')

# Transformando em Maiuscula
print(nome.upper())

# Transformando em Minuscula
print(nome.lower())

# Substituindo o ' ' espaço, por '' string vazia
print(len(nome.replace(' ', '')))

# Dividindo a string em lista e contando o comprimento da primeira lista (0)
print(len(nome.split()[0]))