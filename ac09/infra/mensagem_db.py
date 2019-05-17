import sqlite3
from model.mensagem import Mensagem


def listar():
    con = sqlite3.connect('banco_dados')
    try:
        cur = con.cursor()
        cur.execute('select id, nome from mensagem')
        return [mensagem.cria_de_tupla(el) for el in cur.fetchall()]
    finally:
        con.close()
        
def novo(mensagem):
    con = sqlite3.connect('banco_dados')
    try:
        cur = con.cursor()
        cur.execute("insert into mensagem(id_m, id_r, id_d, data, texto) \
            values (:id_m, :id_r, :id_d, :data, :texto :)", mensagem.__dict__())
        con.commit()
    except:
        con.rollback()
    finally:        
        con.close()