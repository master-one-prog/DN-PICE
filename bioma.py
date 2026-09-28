from abc import ABC, abstractmethod

class Bioma(ABC):
    def __init__(self, temperatura, nome):
        self.nome = nome
        self.temperatura = temperatura
        
class Tundra(Bioma):
    pass

class Floresta_Temperada(Bioma):
    pass

class Deserto(Bioma):
    pass



class Organismo():
    def __init__(self, nome, idade, bioma):
        self.nome = nome
        self.idade = idade
        self.bioma = bioma
        self.hidratacao = 100
        self.temperatura = 36.5
        self.oxigenacao_cerebro = 100
        self.cerebro = Cerebro() 
        self.intestino = Intestino_reto()

    def escalar(self, altura):
        self.oxigenacao_cerebro -= 10 * altura/3000
        if  self.oxigenacao_cerebro >= 95:
            print("ok!")
        # ,,,

    def meditar(self):
        self.impulsos_nervosos 
            
    def mexer_celular(self):
        pass
 
class Intestino_reto():
    pass

class Cerebro():
    pass