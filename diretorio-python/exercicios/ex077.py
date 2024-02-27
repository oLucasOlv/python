lista = ('APRENDER', 'PYTHON', 'Caderno',  'Estojo',
         'Transferidor', 'Compasso', 'Mochila',  'Caneta', 'Livro',)
for palavra in lista:
    vogal = ''
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogal += letra
            vogal += ' '
    print(f'Na palavra {palavra.upper()} temos {vogal.upper()}')
