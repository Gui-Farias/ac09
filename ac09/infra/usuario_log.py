from datetime import datetime
class UsuarioLog():
    def __init__(self, usuario):
        self.original_data = usuario.__dict__()
        self.ultima_atualizacao = usuario.__dict__()
        self.start_time = datetime.now()

    def atualiza(self, usuario):
        self.ultima_atualizacao = usuario.__dict__()

    def finaliza_e_imprime(self):
        print(f'Mudanças iniciaram em {self.start_time}')
        print(f'Valor original:')
        print(self.original_data)
        print(f'Valor final:')
        print(self.ultima_atualizacao)
        print(f'Mudanças finalizaram em {datetime.now()}')