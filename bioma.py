from abc import ABC, abstractmethod
# BIOMAS 


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


# ÓRGÃOS

class Intestino_reto():
    pass

class Cerebro():
    pass
        #self.oxigenacao_cerebro = 100

    def respirar(self):
        pass

    def aumentar_batimento(self):
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

        elif self.oxigenacao_cerebro <= 94 and self.oxigenacao_cerebro >= 90:
            self.cerebro(aumentar_batimento())
            print("!!CUIDADO!! HIPOXEMIA LEVE A MODERADA")
            print("SINTOMAS: Falta de ar / Tontura / Dificuldade para raciocinar ") 

        elif self.oxigenacao_cerebro <= 89 and self.oxigenacao_cerebro >= 85:
            print("!!CUIDADO!! HIPOXEMIA SEVERA")
            print("SINTOMAS: Falta de ar intensa / Tontura forte / inicio de Cianose ")

        elif self.oxigenacao_cerebro <= 84 and self.oxigenacao_cerebro >= 80:
            print("!!CUIDADO!! Os órgãos vitais (cérebro, rins e coração) começam a entrar em sofrimento por falta de oxigênio crônica. O cérebro começa a reduzir suas funções para poupar energia.")
            print("SINTOMAS: letargia, desorientação total no tempo e espaço, extrema dificuldade para falar ou se manter acordado, além de palidez extrema.")
        
        elif self.oxigenacao_cerebro <= 80 and self.oxigenacao_cerebro=>71:
            print("!!CUIDADO!! O cérebro corre risco iminente de sofrer lesões permanentes devido à falta prolongada de oxigenação.")
            print("Perda de consciência (desmaio/coma), convulsões e risco imediato de parada cardiorrespiratória.")    
        else:
            print("VocÊ tem 6 minutos até lesões irreversíveis nas células cerebrais")
            print("Você tem 10 minuros até sua morte, Boa sorte")

    def meditar(self):
        self.impulsos_nervosos 
            
    def mexer_celular(self):
        pass
 
