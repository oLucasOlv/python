salario = float(input('Qual seu Salario atual? R$:'))
n_salario = salario + (salario * 15 / 100)
aumento = n_salario - salario
print('Seu novo salario é de R${:.2f}, com um aumento de R${:.2f}'.format(n_salario,aumento))