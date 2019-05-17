from model.mensagem import Mensagem
from infra.mensagem_log import MensagemLog
from infra.mensagem_db import listar as listar_db, \
    novo as novo_db


def localiza(id):
    for p in listar():
        if p.id == id:
            return p
    return None
    

def novo(mensagem_data):
    novo_db(Mensagem.cria(mensagem_data))
    return listar()