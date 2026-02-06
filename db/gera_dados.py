from faker import Faker
from conectar import conexao, meu_cursor

# configurando Faker
fake =Faker('pt_BR')    

for _ in range(10):
    nome = fake.word().capitalize()
    preco = round(fake.random_number(digits=5) / 100, 2)  # Gerar preço com 2 casas decimais    
    quantidade = fake.random_int(min=1, max=100)
    print(f'Inserindo produto: {nome}, Preço: {preco}, Quantidade: {quantidade}')

    meu_cursor.execute('''
        INSERT INTO PRODUTO (NOME, PRECO, QUANTIDADE)
        VALUES (%s, %s, %s);
    ''', (nome, preco, quantidade))
    
conexao.commit()
print("50 registros inseridos com sucesso na tabela PRODUTO!")
meu_cursor.close()
conexao.close()