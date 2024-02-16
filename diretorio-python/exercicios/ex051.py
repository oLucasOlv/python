pa_inicio = int(input('QUal o Inicio? '))
pa_razao = int(input('QUal o razão? '))

decimo = pa_inicio + (10 - 1) * pa_razao
print('PA:', end='')
for c in range(pa_inicio, decimo, pa_razao):
    print(f'{c}', end=' - ')
