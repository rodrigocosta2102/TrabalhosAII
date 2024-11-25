#Dict para a loja
loja = {
    "produto1": {"nome": "Caderno Espiral A5 Pautado", "preço": 1.80, "quantidade": 54},
    "produto2": {"nome": "Borracha Branca", "preço": 1.30, "quantidade": 157},
    "produto3": {"nome": "Lápis Grafite 2HB", "preço": 4.80, "quantidade": 89},
    "produto4": {"nome": "Mochila Mini Troley Spiderman", "preço": 30, "quantidade": 66 }
}

#Adicionar um novo produto
def add_produto(cod_produto, nome, preco, quantidade):
    produto5 = {"nome": nome, "preço": preco, "quantidade": quantidade}
    loja[cod_produto] = produto5



#Imprimir os produtos
def print_produtos():
    for c,v in loja.items():
        print(c,v)
    print("---------------------------------")

#Atualizar o preço de um produto
def update_produto4(produto4, novo_preco):
    produto4_upd= loja[produto4]
    produto4_upd["preço"]=novo_preco


#Verificar a quantidade em estoque
def verificar_estoque(produto):
    if produto in loja:
        quantidade = loja[produto]["quantidade"]
        return f"A quantidade em estoque de {produto} é: {quantidade}"
    else:
        return f"O produto '{produto}' não está disponível em estoque"
