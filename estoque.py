import json

with open("estoque.json", "r", encoding="utf-8") as f:
    dados = json.load(f)


def encontrar_produto(entrada):
    try:
        codigo = int(entrada)
        for item in dados["estoque"]:
            if item["codigoProduto"] == codigo:
                return item
    except:
        pass

    entrada = entrada.lower()
    for item in dados["estoque"]:
        if entrada in item["descricaoProduto"].lower():
            return item

    return None

while True:
    print("\nMOVIMENTAÇÃO DE ESTOQUE - TARGET SISTEMAS")
    print("Digite 0 para sair.\n")

    entrada = input("Digite o CÓDIGO ou o NOME do produto: ").strip()

    if entrada == "0":
        print("\nSistema encerrado. A Target agradece a sua colaboração!")
        break

    produto = encontrar_produto(entrada)

    if not produto:
        print("Produto não encontrado.")
        continue

    print(f"\nProduto encontrado: {produto['descricaoProduto']}")
    print(f"Estoque atual: {produto['estoque']}\n")

    operacao = input("Você deseja ADICIONAR (A) ou REMOVER (R)? ").strip().upper()

    if operacao not in ("A", "R"):
        print("Operação inválida.")
        continue

    try:
        quantidade = int(input("Quantidade para movimentar: "))
    except ValueError:
        print("Quantidade inválida.")
        continue


    if operacao == "A":
        produto["estoque"] += quantidade
        print(f"\nAdicionado {quantidade} unidades ao estoque.")

    else:
        if quantidade > produto["estoque"]:
            print("\n ERRO: Quantidade maior que o estoque disponível.")
            continue
        produto["estoque"] -= quantidade
        print(f"\nRemovido {quantidade} unidades do estoque.")

    print(f"Estoque final do produto: {produto['estoque']}")

    with open("estoque.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print("Alterações salvas com sucesso!")


