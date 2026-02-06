# pip install faker
# pip install tk    

import psycopg2
from db.conectar import conexao, meu_cursor


# Criar conexão
conexao = psycopg2.connect(
    database="lojadb",
    user="postgres",
    password="admin123",  # ajuste conforme sua senha   
    host="localhost",
    port="5432"
)   
print("Conexão com o Banco de Dados aberta com sucesso!")

# Criação do cursor
meu_cursor = conexao.cursor()

if __name__ == "__main__":
    

    # Criar tabela
    meu_cursor.execute('''
                CREATE TABLE IF NOT EXISTS PRODUTO (
                    CODIGO SERIAL PRIMARY KEY,
                    NOME VARCHAR(100) NOT NULL,
                    PRECO NUMERIC(10, 2) NOT NULL,
                    QUANTIDADE INT NOT NULL 
                );
            ''')

# just in case
conexao.commit()
print("Tabela criada com sucesso!")
conexao.close()