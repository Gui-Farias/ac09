from flask import Blueprint, jsonify, request
from service.mensagem_service import localiza as service_localiza, \
    novo as service_novo
mensagem_app = Blueprint('mensagem_app', __name__, template_folder='templates')


@mensagem_app.route('/mensagem/<int:id_mensagem>', methods=['GET'])
def localiza(id_mensagem):
    a = service_localiza(id_mensagem)
    if(a != None):
        return jsonify(a.__dict__())
    return '', 404


@mensagem_app.route('/mensagem', methods=['POST'])
def novo():
    novo_aluno = request.get_json()
    pr_list = service_novo(novo_mensagem)
    print('exibe com list comprehensions')
    return jsonify([al.__dict__() for al in pr_list])