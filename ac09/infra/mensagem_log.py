from datetime import datetime
class MensagemLog():
    def __init__(self, mensagem):
        self.original_data = mensagem.__dict__()
        self.ultima_atualizacao = mensagem.__dict__()
        self.start_time = datetime.now()

    def atualiza(self, mensagem):
        self.ultima_atualizacao = mensagem.__dict__()

    def finaliza_e_imprime(self):
        print(f'Mudanças iniciaram em {self.start_time}')
        print(f'Valor original:')
        print(self.original_data)
        print(f'Valor final:')
        print(self.ultima_atualizacao)
        print(f'Mudanças finalizaram em {datetime.now()}')
        