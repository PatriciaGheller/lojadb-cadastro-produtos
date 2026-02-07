# Cadastro de Produtos com PostgreSQL e Python

Este projeto demonstra como criar uma aplicação simples para gerenciar produtos em uma loja, utilizando **PostgreSQL** como banco de dados e **Python** com a biblioteca `psycopg2` para realizar operações de CRUD.  
Além disso, a biblioteca **Faker** é usada para gerar dados fictícios e popular a tabela de forma prática durante os testes.

---

## 🚀 Funcionalidades
- Conexão com banco de dados PostgreSQL.
- Criação da tabela `PRODUTO`.
- Inserção de dados fictícios com Faker.
- Interface gráfica em Tkinter para cadastro, atualização, exclusão e listagem de produtos.

---

## 📂 Estrutura do Projeto
cadastro_produtos/
│
├── db/                        # Lógica de banco de dados
│   ├── init.py             # arquivo vazio para marcar como pacote
│   ├── conectar.py              # Conexão com o banco
│   ├── cria_tabela.py          # Criação da tabela PRODUTO
│   ├── gera_dados.py           # Inserção de dados fictícios
│   ├── listar_produtos.py      # Consulta de registros
│   └── app_bd.py               # Classe AppBD com CRUD completo
│
├── gui/                       # Interface gráfica (Tkinter)
│   ├── init.py             # arquivo vazio para marcar como pacote
│   ├── AppGUI.py                # Lógica da interface gráfica
│   └── main_window.py          # Configuração da janela principal
│
├── venv/                      # Ambiente virtual (ignorado pelo Git)
├── main.py                     # Ponto de entrada da aplicação
├── requirements.txt             # Dependências do projeto
└── README.md                    # Documentação


---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/cadastro_produtos.git
   cd cadastro_produtos
    ```
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

- Instale manualmente se necessário:
    ```
    pip install psycopg2-binary faker
    ```
## 🗄️ Banco de Dados
Crie um banco chamado cadastro_produtos (ou ajuste no conectar.py):

    
    CREATE DATABASE cadastro_produtos;

Tabela PRODUTO:

    
    CREATE TABLE IF NOT EXISTS PRODUTO (
    CODIGO SERIAL PRIMARY KEY,
    NOME VARCHAR(100) NOT NULL,
    PRECO NUMERIC(10, 2) NOT NULL,
    QUANTIDADE INT NOT NULL
    );

## ▶️ Executando
Scripts individuais
1. Conectar ao banco:

    ```
    python db/conectar.py
    ```
2. Criar tabela:

    ```
    python db/cria_tabela.py
    ```
3. Inserir dados fictícios:

    ```
    python db/gera_dados.py
    ```
#### Aplicação completa com interface gráfica
    
    python main.py
    
## 📌 Próximos Passos
- Adicionar relatórios e consultas personalizadas.

- Implementar filtros de pesquisa na interface.

- Exportar dados para CSV/Excel.

## 👩‍💻 Autor
Projeto desenvolvido por Patrícia Gheller como prática de integração Python + PostgreSQL.
