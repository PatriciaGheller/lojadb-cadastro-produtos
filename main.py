import tkinter as tk
from db.app_bd import AppBD
from gui.AppGUI import PrincipalBD

def main():
    # Cria a janela principal
    root = tk.Tk()

    # Instancia a classe de banco de dados
    app_bd = AppBD()

    # Instancia a interface gráfica, passando a janela e o banco
    app_gui = PrincipalBD(root, app_bd)

    # Inicia o loop da aplicação
    root.mainloop()

if __name__ == "__main__":
    main()
