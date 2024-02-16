media_idade = 0
idadeMaior = 0
nomeMaior = 0
mulher20 = 0
for pessoa in range(1, 5):
    print(f'-------{pessoa} Pessoa --------')
    nome = input('nome ').strip()
    idade = int(input('idade '))
    sexo = input('sexo [M/F] ').strip()

    if pessoa == 1 and sexo in 'Mm':
        nomeMaior = nome
        idadeMaior = idade
    if sexo in 'Mm' and idade > idadeMaior:
        nomeMaior = nome
        idadeMaior = idade

    elif sexo in 'Ff' and idade < 20:
        mulher20 += 1
    idade += idade
media_idade += idade / 4
print(f'MEDIA IDADE: {media_idade}')
print(f'Homem Velho> {nomeMaior}')
print(f'Mulher 20 anos: {mulher20}')
