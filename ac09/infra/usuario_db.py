import sqlite3
from model.usuario import Usuario


def listar():
    con = sqlite3.connect('banco_dados')
    try:
        cur = con.cursor()
        cur.execute('select id, nome, senha from usuarios')
        return [Usuario.cria_de_tupla(el) for el in cur.fetchall()]
    finally:
        con.close()
        
def novo(usuarios):
    con = sqlite3.connect('banco_dados')
    try:
        cur = con.cursor()
        if usuarios.tipo == "professor":
            cur.execute("insert into professores(id, nome,senha) \
                values (:id, :nome, :senha)", usuarios.__dict__())
        elif usuarios.tipo == "aluno":
            cur.execute("insert into alunos(id, nome,senha) \
                values (:id, :nome, :senha)", usuarios.__dict__())
        con.commit()
    except:
        con.rollback()
    finally:        
        con.close()