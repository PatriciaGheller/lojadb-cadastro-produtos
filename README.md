# Cadastro de Produtos com PostgreSQL e Python

Este projeto demonstra como criar uma aplicação simples para gerenciar produtos em uma loja, utilizando **PostgreSQL** como banco de dados e **Python** com a biblioteca `psycopg2` para realizar operações de CRUD.  
Além disso, a biblioteca **Faker** é usada para gerar dados fictícios e popular a tabela de forma prática durante os testes.

---

## 🚀 Funcionalidades
- Conexão com banco de dados PostgreSQL.
- Criação da tabela `PRODUTO`.
- Inserção de dados fictícios com Faker.
- Estrutura preparada para evoluir com interface gráfica em Tkinter.

---

## 📂 Estrutura do Projeto
cadastro_produtos/
│
├── db/
│   ├── conectar.py       # Conexão com o banco
│   ├── cria_tabela.py   # Criação da tabela PRODUTO
│   └── gera_dados.py    # Inserção de dados fictícios
├── venv/                # Ambiente virtual (ignorado pelo Git)
├── requirements.txt      # Dependências do projeto
└── README.md


---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/cadastro-produtos.git
   cd cadastro-produtos

2. Crie e ative o ambiente virtual:
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```
3. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
## 📦 Dependências

- psycopg2-binary

- Faker

Instale manualmente se necessário:
    ```
    pip install psycopg2-binary faker
    ```
## 🗄️ Banco de Dados
Crie um banco chamado postgres (ou ajuste no conectar.py):
    ```
    CREATE DATABASE postgres;
    ```

Tabela PRODUTO:

    
    CREATE TABLE IF NOT EXISTS PRODUTO (
    CODIGO SERIAL PRIMARY KEY,
    NOME VARCHAR(100) NOT NULL,
    PRECO NUMERIC(10, 2) NOT NULL,
    QUANTIDADE INT NOT NULL
    );
    
## ▶️ Executando
1. Conectar ao banco:
python db/conectar.py

2. Criar tabela:
python db/cria_tabela.py

3. Inserir dados fictícios:
python db/gera_dados.py

## 📌 Próximos Passos
- Implementar interface gráfica com Tkinter.

- Adicionar operações de atualização e exclusão (CRUD completo).

- Criar relatórios e consultas personalizadas.

## 👩‍💻 Autor
Projeto desenvolvido por Patrícia Ghelle como prática de integração Python + PostgreSQL.