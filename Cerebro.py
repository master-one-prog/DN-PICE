class Cerebro():
    def __init__(self):
        self.oxigenacao_cerebro = 100
        self.impulsos_nervosos = 30

    def aumentar_impulsos(self):
        self.impulsos_nervosos += 60

    def diminuir_impulsos(self):
        self.impulsos_nervosos -= 8