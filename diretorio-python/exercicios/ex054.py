from datetime import date
ano_atual = date.today().year

contador_maiores = 0
contador_menores = 0

for c in range(0, 7):
    ano_user = int(input('Ano de Nascimento: '))
    idade = ano_atual - ano_user
    if idade >= 21:
        contador_maiores += 1
    elif idade < 21:
        contador_menores += 1
print(f'{contador_menores} pessoas não alcançaram a maioridade e {
      contador_maiores} já são de maiores')
