import csv

def adicionar_cliente(nome, email, telefone):
    with open('clientes.csv', 'a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, email, telefone])

def visualizar_clientes():
    with open('clientes.csv', 'r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            print(f'Nome: {linha[0]}, Email: {linha[1]}, Telefone: {linha[2]}')

def buscar_cliente(nome):
    with open('clientes.csv', 'r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            if linha[0] == nome:
                print(f'Nome: {linha[0]}, Email: {linha[1]}, Telefone: {linha[2]}')
                return
        print('Cliente não encontrado.')

def main():
    while True:
        print('1. Adicionar cliente')
        print('2. Visualizar clientes')
        print('3. Buscar cliente')
        print('4. Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            nome = input('Nome: ')
            email = input('Email: ')
            telefone = input('Telefone: ')
            adicionar_cliente(nome, email, telefone)
        elif opcao == '2':
            visualizar_clientes()
        elif opcao == '3':
            nome = input('Nome do cliente a ser buscado: ')
            buscar_cliente(nome)
        elif opcao == '4':
            break
        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()
