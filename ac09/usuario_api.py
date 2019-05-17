from flask import Blueprint, jsonify, request
from service.usuario_service import localiza as service_localiza, \
    novo as service_novo 

usuarios_app= Blueprint('usuarios_app', __name__, template_folder='templates')


@usuarios_app.route('/usr/<str:nome>', methods=['GET'])
def localiza(nom):
    a = service_localiza(nom)
    return jsonify({"nome": a.nome})
    


@usuarios_app.route('/usr', methods=['POST'])
def novo():
    nov_usuario= request.get_json()
    pr_list = service_novo(novo_usuario)
    print('exibe com list comprehensions')
    return jsonify({"id": <int>, "segredo": <str>})