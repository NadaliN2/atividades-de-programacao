produtos = {
    "arroz": 25.99,
    "feijao": 9.50,
    "macarrao": 7.99,
    "leite": 5.50,
    "cafe": 14.99,
    "pao": 8.00
}

print("produtos disponíveis no mercado: ", produtos)

produtos_selecionados = []

while True:
    selecionando_produtos = input("Digite um desses produtos: ")
    if selecionando_produtos == "sair":
        break

    if selecionando_produtos in produtos:
        produtos_selecionados.append(selecionando_produtos)
    else:
        print("não, não não não")

precos_compra = []

for produto in produtos_selecionados:
    if produto in produtos:
        preco = produtos[produto]
        precos_compra.append(preco)

total = sum(precos_compra)
print(f"o total da sua compra será de: R$ {total:.2f}")
