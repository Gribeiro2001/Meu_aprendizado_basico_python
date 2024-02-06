# Inicializando a estrutura de dados para armazenar os produtos
estoque = []

def exibir_menu():
    print("========= Menu =========")
    print("1. Adicionar Produto")
    print("2. Atualizar Produto")
    print("3. Visualizar Estoque")
    print("4. Sair do Sistema")
    print("========================")
# Adicionando produto em estoque.
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    
    produto = {"Nome": nome, "Preço": preco, "Quantidade": quantidade}
    estoque.append(produto)
    print("Produto adicionado com sucesso!")
# Atualização do estoque.
def atualizar_produto():
    nome_produto = input("Digite o nome do produto a ser atualizado: ")

    for produto in estoque:
        if produto["Nome"] == nome_produto:
            novo_preco = float(input("Digite o novo preço do produto: "))
            nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
            
            produto["Preço"] = novo_preco
            produto["Quantidade"] = nova_quantidade
            print("Produto atualizado com sucesso!")
            return
    
    print("Produto não encontrado.")

def visualizar_estoque():
    print("========= Estoque =========")
    for produto in estoque:
        print(f"Nome: {produto['Nome']}, Preço: {produto['Preço']}, Quantidade: {produto['Quantidade']}")
    print("============================")

# Loop principal do programa
while True:
    exibir_menu()

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        atualizar_produto()
    elif opcao == "3":
        visualizar_estoque()
    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
