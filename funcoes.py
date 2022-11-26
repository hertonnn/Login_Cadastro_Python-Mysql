from conexão import  criar_conexao, fechar_conexao


def criar_cadastro(nome,senha):

    con = criar_conexao("localhost", "root", "12345678", "Login")

    cursor = con.cursor()

    comando = f'INSERT INTO Cad_Login (nome, senha) VALUES ("{nome}", "{senha}")'
    cursor.execute(comando)
    con.commit()

    cursor.close()
    fechar_conexao(con)

def verifica_user(nome):

    con = criar_conexao("localhost", "root", "12345678", "Login")

    cursor = con.cursor()

    comando = "SELECT id FROM Cad_Login WHERE nome = '{}'".format(nome)
    cursor.execute(comando)
    verifica = cursor.fetchall() # ler o banco de dados

    cursor.close()
    fechar_conexao(con)

    if (len(verifica) != 0):
        return True
    else:
        return False

def verifica_senha(nome, senha):

    con = criar_conexao("localhost", "root", "12345678", "Login")

    cursor = con.cursor()

    comando = "SELECT senha FROM Cad_Login WHERE nome = '{}'".format(nome)
    cursor.execute(comando)
    senha_verifica = cursor.fetchall() # ler o banco de dados

    cursor.close()
    fechar_conexao(con)
    if (senha_verifica [0][0]==  senha):
        return True
    else:
        return False








