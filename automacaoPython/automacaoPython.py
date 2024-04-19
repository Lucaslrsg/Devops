class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class CadastroClientes:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado com sucesso!")

    def visualizar_clientes(self):
        print("\nClientes cadastrados:")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}, Email: {cliente.email}, Telefone: {cliente.telefone}")

    def buscar_cliente(self, nome_busca):
        for cliente in self.clientes:
            if cliente.nome.lower() == nome_busca.lower():
                print(f"Cliente encontrado - Nome: {cliente.nome}, Email: {cliente.email}, Telefone: {cliente.telefone}")
                return
        print(f"Cliente com o nome '{nome_busca}' não encontrado.")

    def atualizar_cliente(self, nome_busca, novo_email, novo_telefone):
        for cliente in self.clientes:
            if cliente.nome.lower() == nome_busca.lower():
                cliente.email = novo_email
                cliente.telefone = novo_telefone
                print(f"Informações do cliente {cliente.nome} atualizadas com sucesso.")
                return
        print(f"Cliente com o nome '{nome_busca}' não encontrado.")

    def excluir_cliente(self, nome_busca):
        for cliente in self.clientes:
            if cliente.nome.lower() == nome_busca.lower():
                self.clientes.remove(cliente)
                print(f"Cliente {cliente.nome} excluído com sucesso.")
                return
        print(f"Cliente com o nome '{nome_busca}' não encontrado.")

def main():
    cadastro = CadastroClientes()

    while True:
        print("\nOpções:")
        print("1. Adicionar cliente")
        print("2. Visualizar clientes")
        print("3. Buscar cliente")
        print("4. Atualizar informações de cliente")
        print("5. Excluir cliente")
        print("6. Encerrar o programa")
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            cliente = Cliente(nome, email, telefone)
            cadastro.adicionar_cliente(cliente)
        elif escolha == "2":
            cadastro.visualizar_clientes()
        elif escolha == "3":
            nome_busca = input("Digite o nome do cliente que deseja buscar: ")
            cadastro.buscar_cliente(nome_busca)
        elif escolha == "4":
            nome_busca = input("Digite o nome do cliente que deseja atualizar: ")
            novo_email = input("Digite o novo email do cliente: ")
            novo_telefone = input("Digite o novo telefone do cliente: ")
            cadastro.atualizar_cliente(nome_busca, novo_email, novo_telefone)
        elif escolha == "5":
            nome_busca = input("Digite o nome do cliente que deseja excluir: ")
            cadastro.excluir_cliente(nome_busca)
        elif escolha == "6":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    main()
