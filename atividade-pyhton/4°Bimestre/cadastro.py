produtos = []
def mostrar_menu():
    print(f"\n1 - Cadastrar produto")
    print("2 - Consultar Produto por ID")
    print("3 - Mostrar os produtos")

    print("s - Sair do Programa")

def  cadastrar_produto():
    id = int(input("\n Digite o ID do produto: "))
    nome = input("Digite o nome produto: ")
    preco = float(input("Digite o preço do produto: \n"))
    produto = {
        "id": id,
        "nome": nome,
        "preco": preco
    }
    produtos.append(produto)

def busca_id(id):
    for produto in produtos:
        if produto["id"] == id:
            print("\nProduto encontrado")
            print(produto)
        else:
            print("\nProduto não encontrado")

def mostrar_produtos():
    for produto in produtos:
        print(f"ID: {produto["id"]}")
        print(f"Nome: {produto["nome"]}")
        print(f"Preco: {produto["preco"]}")

def menu_escolha(escolha):
    match escolha:
        case "1":
            cadastrar_produto()
        case "2":
            id_produto =int(input("Digite o ID" ))
            busca_id(id_produto)
        case "3":
            mostrar_produtos()

while True:
    mostrar_menu()
    escolha =input("\nDIgite a escolha ou [S] para sair: ")
    menu_escolha(escolha)
    if escolha.lower() == "s":
        break