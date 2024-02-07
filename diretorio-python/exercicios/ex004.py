a = input('Digite Algo: \n')



print('Seu tipo é: ', type(a))
print('{} É um numero?' .format(a), a.isnumeric())
print('{} é alfabetico? '.format(a) , a.isalpha())
print('{} É um alfanumerico? '.format(a) , a.isalnum())
print('{} Esta em minusculas? '.format(a) , a.islower())
print('{} Esta em maiuscula? '.format(a) , a.isupper())
print('{} Contem só espaço? '.format(a) , a.isspace())
print('{} Esta capitalizada? '.format(a) , a.istitle())
