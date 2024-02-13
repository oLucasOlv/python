val_casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o valor do seu salário? '))
anos = int(input('Quantos anos deseja pagar a casa? '))

pres_mensal = val_casa / (anos * 12)

if pres_mensal > 30 * sal / 100:
    print('Empréstimo {} NEGADO {}! Pois as prestação execedeu 30% do seu salario!' .format('\033[1;41;97m' , '\033[m'))
else:
    print(f'Empréstimo Concluido com {'\033[1;32m'}SUCESSO{'\033[m'} ! O valor da prestação mensal é de {'\033[1;32m'}R${pres_mensal:.2f} {'\033[m'}' )