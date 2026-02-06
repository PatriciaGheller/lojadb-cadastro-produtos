import psycopg2
from psycopg2 import Error
from faker import Faker
from db.cria_tabela import conexao, meu_cursor


class AppBD:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.conn = psycopg2.connect(
                database="lojadb",
                user="postgres",
                password="admin123",  # ajuste conforme sua senha
                host="127.0.0.1",
                port="5432"
            )
            self.cur = self.conn.cursor()
            print("Conexão com o Banco de Dados aberta com sucesso!")
        except (Exception, Error) as error:
            print("Falha ao se conectar ao Banco de Dados:", error)

    def selecionar_dados(self):
        try:
            self.cur.execute("SELECT * FROM PRODUTO ORDER BY CODIGO")
            registros = self.cur.fetchall()
            return registros
        except (Exception, Error) as error:
            print("Erro ao selecionar dados:", error)
            return []

    def inserir_dados(self, nome, preco, quantidade):
        try:
            self.cur.execute(
                '''INSERT INTO PRODUTO (NOME, PRECO, QUANTIDADE) VALUES (%s, %s, %s)''',
                (nome, preco, quantidade)
            )
            self.conn.commit()
            print("Inserção realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao inserir dados:", error)

    def atualizar_dados(self, codigo, nome, preco, quantidade):
        try:
            self.cur.execute(
                '''UPDATE PRODUTO SET NOME = %s, PRECO = %s, QUANTIDADE = %s WHERE CODIGO = %s''',
                (nome, preco, quantidade, codigo)
            )
            self.conn.commit()
            print("Atualização realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao atualizar dados:", error)

    def excluir_dados(self, codigo):
        try:
            self.cur.execute(
                '''DELETE FROM PRODUTO WHERE CODIGO = %s''',
                (codigo,)
            )
            self.conn.commit()
            print("Exclusão realizada com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao excluir dados:", error)
            
if __name__ == "__main__":
    app_bd = AppBD()
    fake = Faker('pt_BR')

    # Inserir 10 produtos fictícios
    for _ in range(10):
        nome = fake.word().capitalize()
        preco = round(fake.random_number(digits=5) / 100, 2)
        quantidade = fake.random_int(min=1, max=100)
        app_bd.inserir_dados(nome, preco, quantidade)

    # Listar produtos
    produtos = app_bd.selecionar_dados()
    for p in produtos:
        print(p)
