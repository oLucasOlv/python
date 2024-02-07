largura = float(input('Qual a Largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
quantidade = area/ 2  
print('Área: {}² Quantidade de tinta: {:.0f}l'.format(area,quantidade))