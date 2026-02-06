from faker import Faker
from app_bd import AppBD

app_bd = AppBD()
fake = Faker('pt_BR')

# Inserir 5 produtos fictícios
for _ in range(5):
    nome = fake.word().capitalize()
    preco = round(fake.random_number(digits=5) / 100, 2)
    quantidade = fake.random_int(min=1, max=100)
    app_bd.inserir_dados(nome, preco, quantidade)

# Listar produtos
produtos = app_bd.selecionar_dados()
for p in produtos:
    print(p)
