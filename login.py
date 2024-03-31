import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyodbc
from tkcalendar import DateEntry
import datetime






class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")

        # Criando os rótulos e campos de entrada para login
        label_username = tk.Label(root, text="Usuário:")
        label_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        label_password = tk.Label(root, text="Senha:")
        label_password.grid(row=1, column=0, padx=10, pady=5)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        # Definindo os botões para login, cadastro e alterar senha
        button_login = tk.Button(root, text="Login", command=self.login)
        button_login.grid(row=2, column=0, columnspan=3, padx=5, pady=10, sticky="WE")

        button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar)
        button_cadastrar.grid(row=3, column=0, columnspan=3, padx=5, pady=10, sticky="WE")

        button_alterar_senha = tk.Button(root, text="Alterar Senha", command=self.alterar_senha)
        button_alterar_senha.grid(row=4, column=0, columnspan=3, padx=5, pady=10, sticky="WE")

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Conecta-se ao banco de dados
        conn = pyodbc.connect('DRIVER={SQL Server};'
                              'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                              'DATABASE=audiovisual1;'
                              'Trusted_Connection=yes;')
        

        cursor = conn.cursor()

        # Consulta o banco de dados para verificar se o usuário e a senha estão corretos
        cursor.execute("SELECT id_login FROM loginn WHERE usuario = ? COLLATE SQL_Latin1_General_CP1_CS_AS and senha = ? COLLATE SQL_Latin1_General_CP1_CS_AS", (username, password))
        row = cursor.fetchone()

        if row:
            global id_login
            id_login = row[0]  # Obtém o UserID do resultado da consulta
            cursor.close()  # Fecha o cursor
            conn.close()    # Fecha a conexão com o banco de dados
            self.root.withdraw()  # Esconde a janela de login
            import audiovisual 
            
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")

            cursor.close()  # Fecha o cursor
            conn.close()    # Fecha a conexão com o banco de dados

    def cadastrar(self):
        # Abre uma nova janela para cadastro
        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.title("Cadastro de Usuário")

        label_username = tk.Label(cadastro_window, text="Usuário:")
        label_username.grid(row=0, column=0, padx=10, pady=5)
        entry_new_username = tk.Entry(cadastro_window)
        entry_new_username.grid(row=0, column=1, padx=10, pady=5)

        label_password = tk.Label(cadastro_window, text="Senha:")
        label_password.grid(row=1, column=0, padx=10, pady=5)
        entry_new_password = tk.Entry(cadastro_window, show="*")
        entry_new_password.grid(row=1, column=1, padx=10, pady=5)

        def salvar_cadastro():
            new_username = entry_new_username.get()
            new_password = entry_new_password.get()

            # Conecta-se ao banco de dados
            conn = pyodbc.connect('DRIVER={SQL Server};'
                                  'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                                  'DATABASE=audiovisual1;'
                                  'Trusted_Connection=yes;')
            print("conexao realizada")

            cursor = conn.cursor()

            # Verifica se o usuário já existe
            cursor.execute("SELECT * FROM loginn WHERE usuario=? COLLATE SQL_Latin1_General_CP1_CS_AS", (new_username,))
            if cursor.fetchone():
                messagebox.showerror("Cadastro", "Este usuário já existe.")
            else:
                # Insere o novo usuário no banco de dados
                cursor.execute("INSERT INTO loginn (usuario, senha) VALUES (?, ?)", (new_username, new_password))
                conn.commit()
                messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
                cadastro_window.destroy()

            cursor.close()  # Fecha o cursor
            conn.close()    # Fecha a conexão com o banco de dados

        button_salvar_cadastro = tk.Button(cadastro_window, text="Salvar", command=salvar_cadastro)
        button_salvar_cadastro.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

    def alterar_senha(self):
        # Abre uma nova janela para alterar a senha
        alterar_senha_window = tk.Toplevel(self.root)
        alterar_senha_window.title("Alterar Senha")

        label_username = tk.Label(alterar_senha_window, text="Usuário:")
        label_username.grid(row=0, column=0, padx=10, pady=5)
        entry_username = tk.Entry(alterar_senha_window)
        entry_username.grid(row=0, column=1, padx=10, pady=5)

        label_password = tk.Label(alterar_senha_window, text="Nova Senha:")
        label_password.grid(row=1, column=0, padx=10, pady=5)
        entry_new_password = tk.Entry(alterar_senha_window, show="*")
        entry_new_password.grid(row=1, column=1, padx=10, pady=5)

        def salvar_alteracao_senha():
            username = entry_username.get()
            new_password = entry_new_password.get()

            # Conecta-se ao banco de dados
            conn = pyodbc.connect('DRIVER={SQL Server};'
                                  'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                                  'DATABASE=audiovisual1;'
                                  'Trusted_Connection=yes;')

            cursor = conn.cursor()

            # Verifica se o usuário existe
            cursor.execute("SELECT * FROM loginn WHERE usuario=?", (username,))
            if cursor.fetchone():
                # Atualiza a senha do usuário
                cursor.execute("UPDATE loginn SET senha=? WHERE usuario=?", (new_password, username))
                conn.commit()
                messagebox.showinfo("Alterar Senha", "Senha alterada com sucesso!")
                alterar_senha_window.destroy()
            else:
                messagebox.showerror("Alterar Senha", "Usuário não encontrado.")

            cursor.close()  # Fecha o cursor
            conn.close()    # Fecha a conexão com o banco de dados

        button_salvar_alteracao_senha = tk.Button(alterar_senha_window, text="Salvar", command=salvar_alteracao_senha)
        button_salvar_alteracao_senha.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="WE")


root = tk.Tk()
app = LoginApp(root)
root.mainloop()



