from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyodbc
import customtkinter as ctk
from tkcalendar import DateEntry
import datetime






#global id_login

#id_login = 2

root = Tk()

class Limps():
    def limpa_campos(self):
        self.nomeprod.delete(0, END)
        self.combo_genero.delete(0, END)
        self.combo_tipo.delete(0, END)
        self.codigo.delete(0, END)
        self.datassis.delete(0, END)



        


    def salvar_audiovisual(self):
        nome_assis = self.nomeprod.get()
        genero = self.combo_genero.get()
        data_assistido = self.datassis.get()
        producao = self.combo_tipo.get()
    
        
        
        confirmacao = messagebox.askyesno("Confirmação", "Os dados estão corretos?")
        if confirmacao:
            conn = pyodbc.connect('DRIVER={SQL Server};'
                                  'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                                  'DATABASE=audiovisual1;'
                                  'Trusted_Connection=yes;')
            cursor = conn.cursor()

        # Insere o registro do filme assistido na tabela correspondente
            cursor.execute("INSERT INTO audiovisual (id_usuario, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis) VALUES (?, ?, ?, ?, ?)",
                       (id_loginn, nome_assis, producao, genero, data_assistido))
            

            conn.commit()
            conn.close()
            messagebox.showinfo("Audiovisual Assistido", "Armazenado com sucesso!")
            self.realizar_consulta()
            self.limpa_campos()


    def proximo_audiovisual(self):
        proximo = messagebox.askyesno("Inserir Novo Audiovisual", "Deseja inserir outro filme?")
        if proximo:
            # Limpa os campos para inserção de um novo audiovisual
          self.nomeprod.delete(0, END)
          self.combo_genero.delete(0, END)
          self.combo_tipo.delete(0, END)
          self.datassis.delete(0, END)
        else:
          self.limpa_campos()


    def alterar_audiovisual(self):
        nome_assis = self.nomeprod.get()
        genero = self.combo_genero.get()
        data_assistido = self.datassis.get()
        producao = self.combo_tipo.get()
        codigoum = self.codigo.get()
    
        
        
        confirmacao = messagebox.askyesno("Confirmação", "Deseja realmente alterar?")
        if confirmacao:
            conn = pyodbc.connect('DRIVER={SQL Server};'
                                  'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                                  'DATABASE=audiovisual1;'
                                  'Trusted_Connection=yes;')
            cursor = conn.cursor()

        # Insere o registro do filme assistido na tabela correspondente
            cursor.execute("update audiovisual set nomeaudivisual = ?, nome_tipoproduc = ?, nome_gen = ?, data_assis = ? where id_audvis = ?",
                       (nome_assis, producao, genero, data_assistido, codigoum))
            

            conn.commit()
            conn.close()
            messagebox.showinfo("Audiovisual Assistido", "Alterado com sucesso!")
            self.realizar_consulta()
            self.limpa_campos()



    def deletar_audiovisual(self):

        codigoum = self.codigo.get()
    
        
        
        confirmacao = messagebox.askyesno("Confirmação", "Deseja realmente excluir?")
        if confirmacao:
            conn = pyodbc.connect('DRIVER={SQL Server};'
                                  'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                                  'DATABASE=audiovisual1;'
                                  'Trusted_Connection=yes;')
            cursor = conn.cursor()

        # Insere o registro do filme assistido na tabela correspondente
            cursor.execute("delete audiovisual where id_audvis = ?",
                       (codigoum))
            

            conn.commit()
            conn.close()
            messagebox.showinfo("Audiovisual Assistido", "Excluido com sucesso!")
            self.realizar_consulta()
            self.limpa_campos()
            



#criação da classe audiovisual.
class Audiovisual(Limps):
    def __init__(self):      
        self.root = root
        self.tela()
        self.criando_objetos()
        self.lista_audiovisual()
        self.limpa_campos()
        root.mainloop()

#criação da tela    
    def tela(self):
        self.root.title("Gerenciar Audiovisual")
        self.root.configure(background='#EAEAE9')
        self.root.geometry("1200x600")
        self.root.resizable(False, False)

#criação de botões
    def criando_objetos(self):
        #botao salvar
        self.bt_salvar = Button(self.root, text="Salvar", bd=4 , bg='#EAEAE9',fg='#000000', font= ('Times New Roman', 14, 'bold'), command=self.salvar_audiovisual)
        self.bt_salvar.place(relx=0.75, rely=0.04, relwidth=0.20, relheight=0.05)

        #botao Limpar
        self.bt_limpar = Button(self.root, text="Limpar",bd=4, bg='#EAEAE9', fg='#000000', font= ('Times New Roman', 14, 'bold'), command=self.limpa_campos)
        self.bt_limpar.place(relx=0.75, rely=0.10, relwidth=0.20, relheight=0.05)


        #botao alterar
        self.bt_alterar = Button(self.root, text="Alterar",bd=4, bg='#EAEAE9', fg='green', font= ('Times New Roman', 14, 'bold'), command=self.alterar_audiovisual)
        self.bt_alterar.place(relx=0.75, rely=0.16, relwidth=0.20, relheight=0.05)

        #botão Deletar
        self.bt_deletar = Button(self.root, text="Deletar",bd=4, bg='#EAEAE9', fg='red', font= ('Times New Roman', 14, 'bold'), command=self.deletar_audiovisual)
        self.bt_deletar.place(relx=0.75, rely=0.22, relwidth=0.20, relheight=0.05)

       #botão Pesquisar
        self.bt_pesquisar = Button(self.root, text="Pesquisa geral",bd=4, bg='#EAEAE9', fg='blue', font= ('Times New Roman', 14, 'bold'), command=self.realizar_consulta)
        self.bt_pesquisar.place(relx=0.75, rely=0.38, relwidth=0.20, relheight=0.05)
        
        #Radiobutom
        self.rd_filme = Radiobutton(self.root, text="Filme",bd=4, bg='#EAEAE9', fg='Blue', font= ('Times New Roman', 14, 'bold'), command=self.Consulta_filme)
        self.rd_filme.place(relx=0.50, rely=0.38, relwidth=0.20, relheight=0.05)

        self.rd_serie = Radiobutton(self.root, text="Série",bd=4, bg='#EAEAE9', fg='Blue', font= ('Times New Roman', 14, 'bold'), command=self.Consulta_serie)
        self.rd_serie.place(relx=0.40, rely=0.38, relwidth=0.15, relheight=0.05)


        self.rd_documentario = Radiobutton(self.root, text="Documentário",bd=4, bg='#EAEAE9', fg='Blue', font= ('Times New Roman', 14, 'bold'), command=self.Consulta_documentario)
        self.rd_documentario.place(relx=0.28, rely=0.38, relwidth=0.15, relheight=0.05)


        self.rd_anime = Radiobutton(self.root, text="Animação",bd=4, bg='#EAEAE9', fg='Blue', font= ('Times New Roman', 14, 'bold'), command=self.Consulta_animacao)
        self.rd_anime.place(relx=0.15, rely=0.38, relwidth=0.15, relheight=0.05)


        

        #criando label e caixa de texto.
        self.lb_nome = Label(self.root, text="Nome da produção",bg='#EAEAE9', fg='#000000', font= ('Arial', 12, 'bold'))
        self.lb_nome.place(relx=0.0100, rely=0.03, relwidth=0.13, relheight=0.05)
    

        self.nomeprod = Entry(self.root)
        self.nomeprod.place(relx=0.2, rely=0.03, relwidth=0.25, relheight=0.04)

        #Genero
        self.lb_genero = Label(self.root, text="Gênero", bg='#EAEAE9',fg='#000000', font= ('Arial', 12, 'bold'))
        self.lb_genero.place(relx=0.00, rely=0.09, relwidth=0.10, relheight=0.05)
        

        generos = ["Ação", "Comédia", "Drama", "Romance", "Ficção Científica", "Terror","Reality","Documentário","Espionagem","Fantasia","Filme de guerra","Musical","Filme policial"]
        self.combo_genero = ttk.Combobox(root, values= generos)
        self.combo_genero.place(relx=0.20, rely=0.09, relwidth=0.10, relheight=0.05)

        #Tipo de produção
        self.lb_tipo = Label(self.root, text="Tipo de produção", bg='#EAEAE9',fg='#000000', font= ('Arial', 12, 'bold'))
        self.lb_tipo.place(relx=0.0, rely=0.15, relwidth=0.14, relheight=0.05)
       

        tipopro = ["Filme", "Série", "Documentário","Animação"]
        self.combo_tipo = ttk.Combobox(root, values= tipopro)
        self.combo_tipo.place(relx=0.20, rely=0.15, relwidth=0.08, relheight=0.05)

        #Data assistida
        self.lb_calendario = Label(self.root, text="Data assistida", bg='#EAEAE9',fg='#000000', font= ('Arial', 12, 'bold'))
        self.lb_calendario.place(relx=0.01, rely=0.22, relwidth=0.10, relheight=0.05)
        

        
        self.datassis = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.datassis.place(relx=0.20, rely=0.22, relwidth=0.08, relheight=0.05)



        self.lb_nome = Label(self.root, text="Código",bg='#EAEAE9', fg='#000000', font= ('Arial', 12, 'bold'))
        self.lb_nome.place(relx=0.01, rely=0.35, relwidth=0.13, relheight=0.05)
        self.codigo = Entry(self.root)
        self.codigo.place(relx=0.045, rely=0.40, relwidth=0.05, relheight=0.03)


  
    
    

    


    def lista_audiovisual(self):
        self.listaudi = ttk.Treeview(self.root, height= 3, columns=("col1", "col2", "col3", "col4","col5"))
        self.listaudi.heading("#0", text="")
        self.listaudi.heading("#1", text="Código")
        self.listaudi.heading("#2", text="Nome")
        self.listaudi.heading("#3", text="Gênero")
        self.listaudi.heading("#4", text="Produção")
        self.listaudi.heading("#5", text="Data Assistida")

        self.listaudi.column("#0", width=1)
        self.listaudi.column("#1", width=50)
        self.listaudi.column("#2", width=200)
        self.listaudi.column("#3", width=125)
        self.listaudi.column("#4", width=125)
        self.listaudi.column("#5", width=125)


        self.listaudi.place(relx=0.01, rely=0.45, relwidth=0.97, relheight=0.54)


        self.scroolistaudi =Scrollbar(self.root, orient='vertical')
        self.listaudi.configure(yscroll=self.scroolistaudi.set)
        self.scroolistaudi.place(relx=0.96, rely=0.45, relwidth=0.04,relheight=0.54)
        self.listaudi.bind("<Double-1>", self.ondoubleClick)


    def formatar_data(self, data):
    # Formatar data para o padrão brasileiro (dd/mm/aaaa)
        data_datetime = datetime.datetime.strptime(data, '%Y-%m-%d')
        return data_datetime.strftime('%d/%m/%Y')



    def realizar_consulta(self):
        


        conn = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                            'DATABASE=audiovisual1;'
                            'Trusted_Connection=yes;')
        cursor = conn.cursor()
        

        if id_login:
            cursor.execute("SELECT id_audvis, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis FROM audiovisual where id_usuario =?", id_login)
            
        else:
            cursor.execute("SELECT id_audvis, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis FROM audiovisual where id_usuario =?", id_login)

        resultados = cursor.fetchall()

        self.listaudi.delete(*self.listaudi.get_children())


        for resultado in resultados:
            data_formatada = self.formatar_data(resultado[4])
            self.listaudi.insert("", "end", values=(resultado[0], resultado[1], resultado[2], resultado[3], data_formatada))

        cursor.close()
        conn.close()


    def Consulta_filme(self):
       


        conn = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                            'DATABASE=audiovisual1;'
                            'Trusted_Connection=yes;')
        cursor = conn.cursor()
        

        if id_login:
            cursor.execute("SELECT id_audvis, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis FROM audiovisual where audiovisual.nome_tipoproduc = ? and audiovisual.id_usuario = ?", ("Filme", id_login))
            
        else:
            cursor.execute("SELECT id_audvis, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis FROM audiovisual where audiovisual.nome_tipoproduc = ? and audiovisual.id_usuario = ?", ("Filme", id_login))

        resultados = cursor.fetchall()

        self.listaudi.delete(*self.listaudi.get_children())


        for resultado in resultados:
            data_formatada = self.formatar_data(resultado[4])
            self.listaudi.insert("", "end", values=(resultado[0], resultado[1], resultado[2], resultado[3], data_formatada))

        cursor.close()
        conn.close()


    def Consulta_serie(self):
       


        conn = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                            'DATABASE=audiovisual1;'
                            'Trusted_Connection=yes;')
        cursor = conn.cursor()
        

        if id_login:
            cursor.execute("SELECT id_audvis, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis FROM audiovisual where audiovisual.nome_tipoproduc = ? and audiovisual.id_usuario = ?", ("Série",id_login))
            
        else:
            cursor.execute("SELECT id_audvis, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis FROM audiovisual where audiovisual.nome_tipoproduc = ? and audiovisual.id_usuario = ?", ("Série",id_login))

        resultados = cursor.fetchall()

        self.listaudi.delete(*self.listaudi.get_children())


        for resultado in resultados:
            data_formatada = self.formatar_data(resultado[4])
            self.listaudi.insert("", "end", values=(resultado[0], resultado[1], resultado[2], resultado[3], data_formatada))

        cursor.close()
        conn.close()


    def Consulta_documentario(self):
       


        conn = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                            'DATABASE=audiovisual1;'
                            'Trusted_Connection=yes;')
        cursor = conn.cursor()
        

        if id_login:
            cursor.execute("SELECT id_audvis, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis FROM audiovisual where audiovisual.nome_tipoproduc = ?  and id_usuario = ?", ("Documentário", id_login))
            
        else:
            cursor.execute("SELECT id_audvis, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis FROM audiovisual where audiovisual.nome_tipoproduc = ? and id_usuario = ?", ("Documentário", id_login))

        resultados = cursor.fetchall()

        self.listaudi.delete(*self.listaudi.get_children())


        for resultado in resultados:
            data_formatada = self.formatar_data(resultado[4])
            self.listaudi.insert("", "end", values=(resultado[0], resultado[1], resultado[2], resultado[3], data_formatada))

        cursor.close()
        conn.close()


    def Consulta_animacao(self):
       


        conn = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=DTI-NBRPE07DXG9\SQLEXPRESS;'
                            'DATABASE=audiovisual1;'
                            'Trusted_Connection=yes;')
        cursor = conn.cursor()
        

        if id_login:
            cursor.execute("SELECT id_audvis, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis FROM audiovisual where audiovisual.nome_tipoproduc = ? and audiovisual.id_usuario = ?", ("Animação", id_login))
            
        else:
            cursor.execute("SELECT id_audvis, nomeaudivisual, nome_tipoproduc, nome_gen, data_assis FROM audiovisual where audiovisual.nome_tipoproduc = ? and audiovisual.id_usuario = ?", ("Animação", id_login))

        resultados = cursor.fetchall()

        self.listaudi.delete(*self.listaudi.get_children())


        for resultado in resultados:
            data_formatada = self.formatar_data(resultado[4])
            self.listaudi.insert("", "end", values=(resultado[0], resultado[1], resultado[2], resultado[3], data_formatada))

        cursor.close()
        conn.close()


    def ondoubleClick(self, event):
        self.limpa_campos()
        self.listaudi.selection()

        for n in self.listaudi.selection():
            col1, col2, col3, col4, col5 = self.listaudi.item(n, 'values')
            self.codigo.insert(END, col1)
            self.nomeprod.insert(END, col2)
            self.combo_genero.insert(END, col4)
            self.combo_tipo.insert(END, col3)
            self.datassis.insert(END, col5)



        

Audiovisual()




