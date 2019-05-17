class Usuario():
    def __init__(self, id, nome,tipo):
        caracteres = "0123456789abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@!#$%&*()_+}{`^?;:>/-+.,"
        senha = ""
        for i in range(10):
            senha += choice(caracteres)
        self.id = id
        self.nome = nome
        self.senha = senha
        self.tipo = tipo

        
    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            senha = dados["senha"]
            tipo = dados["tipo"]
            return Usuario(id=id, nome=nome,senha=senha,tipo=tipo)
        except Exception as e:
            print("Problema ao criar novo usuário!")
            print(e)

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            nome = dados[1]
            senha = dados[2]
            return Usuario(id=id, nome=nome,senha=senha)
        except Exception as e:
            print("Problema ao criar novo usuario!")
            print(e)
