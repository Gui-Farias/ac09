class Mensagem():
    def __init__(self, id_m, id_r,id_d,data,texto):
        self.id_m = id_m
        self.id_r = id_r
        self.id_d = id_d
        self.data = data
        self.texto = texto
        
    @staticmethod
    def cria(dados):
        try:
            id_m = dados["id_m"]
            id_r = dados["id_r"]
            id_d= dados["id_d"]
            data= dados["data"]
            texto= dados["texto"]
            return Mensagem(id_m=id_m, id_r=id_r,id_d=id_d,data=data,texto=texto)
        except Exception as e:
            print("Problema ao criar nova mensagem!")
            print(e)
            
    @staticmethod
    def cria_de_tupla(dados):
        try:
            id_m = dados[0]
            id_r = dados[1]
            id_d = dados[2]
            data = dados[3]
            texto = dados[4]
            return Mensagem(id_m=id_m, id_r=id_r,id_d=id_d,data=data,texto=texto)
        except Exception as e:
            print("Problema ao criar nova mensagem!")
            print(e)