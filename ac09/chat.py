from flask import Flask, jsonify, request
from usuario_api import usuarios_app
from mensagem_api import mensagem_app
import sqlite3

app = Flask(__name__)
app.register_blueprint(usuarios_app)
app.register_blueprint(mensagem_app)

if __name__ == "__main__":
    res = input('deseja criar o bd?')
    if res == "s":
        con = sqlite3.connect("banco_dados")
        cur = con.cursor()
        cur.execute("create table usuario (\
            id integer, \
            nome varchar(50),\
            senha varchar(50) )")

        cur.execute("create table mensagem (\
            id_m integer, \
            id_r smallint,\
            id_d smallint,\
            data date, \
            texto varchar(500) )")
        con.commit()
        con.close()
    app.run(host='localhost', port=5000, debug=True)