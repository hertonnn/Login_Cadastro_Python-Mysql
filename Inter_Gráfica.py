import tkinter
from tkinter import *
from tkinter import messagebox

from funcoes import *


# ------------------ Parte Gráfica -------------------------
# cores --------------------------------------------------------

co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"  # letra / letters


# ------------------ Parte  cadastro-------------------------
def tela_cadastro():

    def cadastro():
        nome = str(e_nome.get())
        senha = str(e_senha.get())

        if (len(nome) < 5 or len(senha) < 5):
            messagebox.showwarning("Erro", "Usuário e/ou senha inválidos ", parent=janela_cad)
            return 0
        if (not verifica_user(nome)):
            criar_cadastro(nome, senha)
            ok = messagebox.askokcancel("Cadastrado com sucesso!", "Voltar ao login?", parent=janela_cad)
            if(ok):
                janela_cad.destroy()
            else:
                return 0
        messagebox.showwarning("Erro", "Usuário já existente", parent=janela_cad)
        return 0

    # ------------------ Parte Gráfica (cadastro)-------------------------

    janela_cad = tkinter.Toplevel()
    janela_cad.geometry("310x300")
    janela_cad.title('Cadastro')
    janela_cad.config(background=co1)
    janela_cad.resizable(width=False, height=False)



    l_nome = Label( janela_cad, text='CADASTRO', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5, )

    l_linha = Label( janela_cad, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co3, fg=co4)
    l_linha.place(x=10, y=45)

    # Configurando entrada de dados ------------------------------------------

    l_nome = Label(janela_cad, text='Nome* ', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=10, y=60)
    e_nome = Entry(janela_cad, width=20, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    e_nome.place(x=14, y=80)

    l_senha = Label( janela_cad, text='Senha* ', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_senha.place(x=10, y=120)
    e_senha = Entry( janela_cad, width=20, justify='left', show='*', font=("", 15), highlightthickness=1,
                    relief='solid')
    e_senha.place(x=14, y=140)

    b_confirmar = Button( janela_cad, command=cadastro, text='Cadastrar', width=10, height=2, anchor=NW,
                         font=('Ivy 8 bold'), bg=co3, fg=co1, relief=RAISED, overrelief=RIDGE)
    b_confirmar.place(x=105, y=180)

    janela_login.mainloop()


def login():
    nome = str(e_nome.get())
    senha = str(e_senha.get())

    if( not verifica_user(nome)):
        messagebox.showwarning("Erro", "Usuário não existe ")
    if(verifica_senha(nome,senha)):
        janela_login.destroy()
        messagebox.showinfo("Logado", "Bem vindo " + nome)

    else:
        messagebox.showwarning("Erro", "Senha inválida ")



# ------------------ Parte Gráfica (Login)-------------------------

janela_login = Tk()
janela_login.geometry("310x300")
janela_login.title('Login')
janela_login.config(background=co1)
janela_login.resizable(width=False, height=False)



# Configurando entrada de dados------------------------------------------

l_nome = Label(janela_login, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5, )

l_linha = Label(janela_login, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co3, fg=co4)
l_linha.place(x=10, y=45)


l_nome = Label(janela_login, text='Nome* ', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=60)
e_nome = Entry(janela_login, width=20, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=80)

l_senha = Label(janela_login, text='Senha* ', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_senha.place(x=10, y=120)
e_senha = Entry(janela_login, width=20, justify='left', show='*', font=("", 15), highlightthickness=1,
                relief='solid')
e_senha.place(x=14, y=140)

b_confirmar = Button(janela_login, command=login, text='Entrar', width=10, height=2, anchor=NW,
                     font=('Ivy 8 bold'), bg=co3, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)

b_confirmar = Button(janela_login, command=tela_cadastro, text='Cadastrar', width=10, height=2, anchor=NW,
                     font=('Ivy 8 bold'), bg=co3, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=105, y=180)

janela_login.mainloop()
