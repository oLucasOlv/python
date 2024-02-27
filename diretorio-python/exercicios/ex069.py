
# sex = input('Sexo: ').upper().strip()[0]
# idade = int(input('Idade: '))
r = 'S'
pessoas18 = homens = mulheres20 = 0
while True:
    sex = input('Sexo: ').upper().strip()[0]
    while sex in 'MF' and r == 'S':
        idade = int(input('Idade: '))
        if sex in 'M':
            homens += 1
        elif sex in 'F' and idade < 20:
            mulheres20 += 1
        elif idade > 18:
            pessoas18 += 1
        
        r = input('Deseja Continuar? ').upper().strip()[0]
        while r not in 'SN':
            r = input('Deseja Continuar? ').upper().strip()[0]

        if r == 'N':
            print(f'\nPessoas com mais de 18 anos: {pessoas18}\n Homens Cadastrados: {homens}\n Mulheres com menos de 20 anos: {mulheres20}')
            break
        
        sex = input('Sexo: ').upper().strip()[0]
    if r == 'N':
        break
print(f'ACABOU!')
