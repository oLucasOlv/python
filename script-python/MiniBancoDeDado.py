import re
import csv
import os
from tabulate import tabulate


regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def verificar_email(email, arquivo_cvs='./tabela.csv'):
    try:
        with open(arquivo_cvs, 'r') as csvfile:
            linhas = csvfile.readlines()

            for linha in linhas[1:]:
                if email in linha:
                    return True
        return False

    except FileNotFoundError:
        print(f'O arquivo {arquivo_cvs} não foi encontrado!')
        return False


def check(email):
    if re.search(regex, email):

        return True
    else:

        return False


def coletar_email():
    while True:
        email = input('Digite Seu Email: ').strip()
        if check(email) and not verificar_email(email):
            return email
        print('Email já Cadastrado ou Formato do Email Inválido')


def coletar_nome():
    while True:
        nome = input('Digite Seu Nome: ').strip()
        if nome.isalpha():
            return nome
        print('Caractere Inválido\n')


def coletar_idade():
    while True:
        idade = input('Digite Sua Idade: ').strip()
        if idade.isdigit() and int(idade) > 0:
            return idade
        print('Caractere Inválido\n')


def buscar_registro(email):
    with open('./tabela.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
     
            for linha in reader:
                if email == linha[2]:
                   return linha
    
    return print(f"O email '{email}' não foi Cadastrado!\n")

while True:

    print("1 . Adicionar Registro: ")
    print("2 . Exibir Todos os Registro: ")
    print("3 . Buscar Registro: ")
    print("4 . Sair: ")
    user_opcao = int(input('\n Digite uma Opção: '))

    if user_opcao == 1:
        part_exist = os.path.exists('./tabela.csv')
        with open('./tabela.csv', 'a', newline='') as csvfile:
            write = csv.writer(csvfile)

            if not part_exist or os.stat('./tabela.csv').st_size == 0:
                write.writerow(['Nome', 'Idade', 'Email'])

            dados = [

                coletar_nome(),
                coletar_idade(),
                coletar_email()
            ]
            write.writerow(dados)

    elif user_opcao == 2:
        with open('./tabela.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            linha = [linha for linha in reader]
            if linha:
                print(tabulate(linha, headers= 'firstrow', tablefmt='grid'))
        print('\n')

    elif user_opcao == 3:
        while True:
            print("1 . Digite seu Email: ")
            print("2 . Sair: ")
            user_opcao = int(input('\n Digite uma Opção: '))
            if user_opcao == 1 :
                email = input('\n : ').strip()
                if buscar_registro(email) != None:
                    print(' | '.join(buscar_registro(email)))
                    break
            elif user_opcao == 2 :
                break
            elif user_opcao != 1 and 2:
                print('Opção Inválida! \n')
                continue

    elif user_opcao == 4:
        os.system('cls')
        break
