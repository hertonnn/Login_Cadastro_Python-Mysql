import mysql.connector


def criar_conexao(host, usuario, senha, banco):
        return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco, auth_plugin='mysql_native_password' )

def fechar_conexao(con):
    return con.close()