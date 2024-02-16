frase = input('Digite uma Frase: ')

frase = frase.replace(' ', '').replace('-', '').replace('_', '').lower()
frase_reverse = frase[::-1].lower()

verificacao = False
for c in range(1, len(frase) + 1):
    if frase[c-1:c] == frase_reverse[c-1:c]:
        verificacao = True
if verificacao == True:
    print('Palíndromo',)
else:
    print('Não é palíndromo')
