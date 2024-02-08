
from random import choice

n1 = str(input('Primeiro Aluno: '))
n2 = input('Segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('Quinto aluno: ')

lista = [n1, n2, n3, n4]

escolhido = choice(lista)
   
print(f'Quem ira apagar o quadro sera {escolhido}')