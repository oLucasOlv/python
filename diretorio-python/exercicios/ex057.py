sex = input('Qual seu sexo (M/F)? ').strip().upper()[0]

while sex not in "FM":
    sex = input('Qual seu sexo (M/F)? ').strip().upper()[0]
    if sex not in "FM":
        print('Sexo invalido, Tente Novamente')


print('Fim!')
