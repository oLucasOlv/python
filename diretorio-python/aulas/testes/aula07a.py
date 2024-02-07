n1 = int(input('Digite um número: '))
n2 = int(input('Digite um Segundo Número: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
div = n1 / n2
div_int = n1 // n2
res = n1 % n2 
pot = n1**n2

print(' Soma: {}\n Subtração: {}\n Multiplicação: {}\n Divisão: {:.2f}' .format(s,sub,m,div), end='\n')
print(' Divisão Inteira: {}\n Resto da Divisão: {}\n Potencia: {}' .format(div_int,res,pot))