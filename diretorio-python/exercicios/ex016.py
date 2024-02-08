from math import floor #importando a função floor do metodo math

num = float(input('Digite uma número: ')) #armazenadno o número do usuario

num_int = floor(num) # aredondando o número Real para o número menor

print(f'O número {num:.3f} tem a parte inteira {num_int}')