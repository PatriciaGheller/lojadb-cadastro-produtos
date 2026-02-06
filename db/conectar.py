import psycopg2

# Criar conexão
conexao = psycopg2.connect(
    database="lojadb",
    user="postgres",
    password="admin123",
    host="localhost",
    port="5432"
)
print("Banco de dados conectado com sucesso!")

# Criar cursor
meu_cursor = conexao.cursor()