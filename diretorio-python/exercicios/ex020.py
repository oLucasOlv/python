from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quinto aluno: ')

nomes = [a1, a2, a3, a4]

shuffle(nomes) # embaralhar itens

# not working good sec = choices(nomes, weights=[1,1,1,1], k=4)

print(f'a sequencia sera: {nomes}')