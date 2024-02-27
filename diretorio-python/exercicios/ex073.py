tabela = ('Palmeiras', 'Gremio', 'Atletico Mineiro', 'Flamengo', 'Botafogo', 'Bragantino', "Fluminense", "Paranaense", "Internacional",
          "Fortaleza", "São Paulo", "Chapecoence", "Corinthians", "Cruzeiro", "Vasco Da Gama", "Bahia", "Santos", "Goias", "Coritiba", "America MG")


print(f'Lista de times do Brasileirão {tabela}')
print('-=' *10)

print(f'Os 5 primeiras são {tabela[0:5]}')
print('-=' *10)

print(f'Os 4 últimos são {tabela[-4:]}')
print('-=' *10)

print(f'Tabela em ordem Alfabetica {sorted(tabela)}')
print('-=' *10)

print(f'Chapecoence esta em {tabela.index('Chapecoence') + 1}º posição')