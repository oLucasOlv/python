city = input('Digite o nome da Cidade: ')

city = city.split()
print(f'Começa com "Santo"? {'SANTO' in city[0].upper()}')