from model.usuario import Usuario
from infra.usuario_log import UsuarioLog
from infra.usuario_db import listar as listar_db, \
    novo as novo_db


def localiza(nome):
    for p in listar():
        if p.nome == nome:
            return p
    return None
    

def novo(usuario_data):
    novo_db(Usuario.cria(usuario_data))
    return listar()