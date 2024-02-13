val_casa = float(input('Valor casa: R$'))
sal = float(input('Salário do Comprador: R$'))
anos = int(input('Quantos anos de finaciamento? '))

pres_mensal = val_casa / (anos * 12)

if pres_mensal >= sal * 30 / 100:
    print('Empréstimo {} NEGADO {}! Pois as prestação execedeu 30% do seu salario!' .format('\033[1;41;97m' , '\033[m'))
else:
    print(f'Empréstimo Concluido com {'\033[1;32m'}SUCESSO{'\033[m'} ! Para pagar em {anos} anos o valor da prestação mensal é de {'\033[1;32m'}R${pres_mensal:.2f} {'\033[m'}' )