# Sistema simples de controle de estoque em Python
# Desenvolvido para o PIM I - UNIP

produtos = []

def exibir_menu():
    print("\n--- MENU DO ESTOQUE ---")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Vender produto")
    print("4 - Sair")

def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    preco = float(input("Preço do produto: R$ ").replace(",", "."))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    print("\n--- PRODUTOS CADASTRADOS ---")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"Nome: {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Estoque: {produto['quantidade']}"
        )

def encontrar_produto(nome_procurado):
    for produto in produtos:
        if produto["nome"].lower() == nome_procurado.lower():
            return produto
    return None

def vender_produto():
    nome_venda = input("Digite o nome do produto vendido: ").strip()
    produto = encontrar_produto(nome_venda)

    if produto is None:
        print("Produto não encontrado.")
        return

    quantidade_venda = int(input("Quantidade vendida: "))

    if quantidade_venda <= produto["quantidade"]:
        produto["quantidade"] -= quantidade_venda
        total = quantidade_venda * produto["preco"]
        print(f"Venda realizada com sucesso! Total: R$ {total:.2f}")
        print(f"Estoque atualizado: {produto['quantidade']} unidade(s).")
    else:
        print("Estoque insuficiente para realizar a venda.")

def executar_sistema():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            vender_produto()
        elif opcao == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar_sistema()
