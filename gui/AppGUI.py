import tkinter as tk
from tkinter import ttk
from db.app_bd import AppBD

class PrincipalBD:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Cadastro de Produtos")
        self.root.geometry("600x400")
        self.create_widgets()
        self.carregarDadosIniciais()

    def create_widgets(self):
        # Labels e Entradas
        self.lblCodigo = tk.Label(self.root, text="Código")
        self.lblCodigo.grid(row=0, column=0)
        self.txtCodigo = tk.Entry(self.root)
        self.txtCodigo.grid(row=0, column=1)

        self.lblNome = tk.Label(self.root, text="Nome")
        self.lblNome.grid(row=1, column=0)
        self.txtNome = tk.Entry(self.root)
        self.txtNome.grid(row=1, column=1)

        self.lblPreco = tk.Label(self.root, text="Preço")
        self.lblPreco.grid(row=2, column=0)
        self.txtPreco = tk.Entry(self.root)
        self.txtPreco.grid(row=2, column=1)

        self.lblQuantidade = tk.Label(self.root, text="Quantidade")
        self.lblQuantidade.grid(row=3, column=0)
        self.txtQuantidade = tk.Entry(self.root)
        self.txtQuantidade.grid(row=3, column=1)

        # Botões
        self.btnCadastrar = tk.Button(self.root, text="Cadastrar", command=self.fCadastrarProduto)
        self.btnCadastrar.grid(row=4, column=0)
        self.btnAtualizar = tk.Button(self.root, text="Atualizar", command=self.fAtualizarProduto)
        self.btnAtualizar.grid(row=4, column=1)
        self.btnExcluir = tk.Button(self.root, text="Excluir", command=self.fExcluirProduto)
        self.btnExcluir.grid(row=5, column=0)
        self.btnLimpar = tk.Button(self.root, text="Limpar", command=self.fLimparTela)
        self.btnLimpar.grid(row=5, column=1)

        # Treeview
        self.tree = ttk.Treeview(self.root, columns=("CODIGO", "NOME", "PRECO", "QUANTIDADE"), show="headings")
        self.tree.heading("CODIGO", text="Código")
        self.tree.heading("NOME", text="Nome")
        self.tree.heading("PRECO", text="Preço")
        self.tree.heading("QUANTIDADE", text="Quantidade")
        self.tree.grid(row=6, column=0, columnspan=2)
        self.tree.bind('ButtonRelease-1', self.apresentarRegistrosSelecionados)

    def fCadastrarProduto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        quantidade = self.txtQuantidade.get()
        self.db.inserir_dados(nome, preco, quantidade)
        self.tree.insert("", "end", values=(codigo, nome, preco, quantidade))
        self.fLimparTela()

    def fAtualizarProduto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        quantidade = self.txtQuantidade.get()
        self.db.atualizar_dados(codigo, nome, preco, quantidade)
        selected_item = self.tree.selection()[0]
        self.tree.item(selected_item, values=(codigo, nome, preco, quantidade))
        self.fLimparTela()

    def fExcluirProduto(self):
        codigo = self.txtCodigo.get()
        self.db.excluir_dados(codigo)
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)
        self.fLimparTela()
        self.carregarDadosIniciais()

    def fLimparTela(self):
        self.txtCodigo.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtPreco.delete(0, tk.END)
        self.txtQuantidade.delete(0, tk.END)

    def apresentarRegistrosSelecionados(self, event):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, "values")
        self.txtCodigo.delete(0, tk.END)
        self.txtCodigo.insert(0, values[0])
        self.txtNome.delete(0, tk.END)
        self.txtNome.insert(0, values[1])
        self.txtPreco.delete(0, tk.END)
        self.txtPreco.insert(0, values[2])
        self.txtQuantidade.delete(0, tk.END)
        self.txtQuantidade.insert(0, values[3])

    def carregarDadosIniciais(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        registros = self.db.selecionar_dados()
        for registro in registros:
            self.tree.insert("", "end", values=registro)

# Criando a interface gráfica
root = tk.Tk()
app_bd = AppBD()
app_gui = PrincipalBD(root, app_bd)
root.mainloop()
