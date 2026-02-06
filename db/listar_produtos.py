from conectar import conexao, meu_cursor

try:
    # Consultar todos os produtos
    meu_cursor.execute("SELECT CODIGO, NOME, PRECO, QUANTIDADE FROM PRODUTO;")
    produtos = meu_cursor.fetchall()

    print("Lista de produtos cadastrados:\n")
    for produto in produtos:
        codigo, nome, preco, quantidade = produto
        print(f"Código: {codigo} | Nome: {nome} | Preço: R${preco:.2f} | Quantidade: {quantidade}")

except Exception as e:
    print("Erro ao listar produtos:", e)
finally:
    meu_cursor.close()
    conexao.close()
