frase = input('Digite uma Frase: ')
frase = frase.replace('ã', 'a').upper()
vezes = frase.count('A') # contando 
posicao_i = frase.find('A') # procurando da esquerda para direita
posicao_f = frase.rfind('A') # procurando da direita para esquerda

print(f'Quantas vezes apareceu: {vezes} Primeira Posição a Aparecer: {posicao_i} Última posição a Aparcer: {posicao_f}')