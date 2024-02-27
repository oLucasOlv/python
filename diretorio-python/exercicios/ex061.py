pa_inicio = int(input('QUal o Inicio? '))
pa_razao = int(input('QUal o razão? '))

termo = pa_inicio
c = 1

while c <= 10:
    print(f'{termo} > ', end=' ')
    termo += pa_razao
    c += 1