import tkinter as tk
from db.app_bd import AppBD
from gui.AppGUI import PrincipalBD

def criar_janela():
    root = tk.Tk()
    root.title("Cadastro de Produtos")
    root.geometry("600x400")

    app_bd = AppBD()
    PrincipalBD(root, app_bd)

    return root

if __name__ == "__main__":
    janela = criar_janela()
    janela.mainloop()
