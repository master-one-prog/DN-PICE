
from abc import ABC, abstractmethod
# BIOMAS 


class Bioma(ABC):
    def __init__(self, estacao, nome):
        self.nome = nome
        self.estacao = estacao

    @abstractmethod
    def efeito_bioma(self):
        pass

class Tundra(Bioma):
    def __init__(self, estacao, nome):
        super().__init__(estacao, nome)
        
        if self.estacao == "inverno":
            self.temperatura = -50
        
        elif self.estacao == "verão":
            self.temperatura = 12

        else:
            self.temperatura = 0

    def efeito_bioma(self):
        if self.estacao =="inverno":
            self.coracao.aumentar_batimento += 15
            self.organismo.temperatura -= 2
        
        elif self.estacao == "verão":
            self.organismo.batimento += 10
            self.organismo.temperatura -= 1

        else:
            self.organismo.batimento += 7
            self.organismo.temperatura -= 0.5


    


class Floresta_Temperada(Bioma):
    def __init__(self, estacao, nome):
        super().__init__(estacao, nome)

        if self.estacao == "inverno":
            self.temperatura = 0
                
        elif self.estacao == "verão":
            self.temperatura = 22
        
        else:
            self.temperatura = 15

    def efeito_bioma(self):
        if self.estacao =="inverno":
            self.organismo.hidratacao -= 7
            
        
        elif self.estacao == "verão":
            self.organismo.hidratacao -= 15
            

        else:
            self.organismo.hidratacao -= 10
            
        

class Deserto(Bioma):
    def __init__(self, estacao, nome):
        super().__init__(estacao, nome)

        if self.estacao == "inverno":
            self.temperatura = 15
                
        elif self.estacao == "verão":
            self.temperatura = 40
        
        else:
            self.temperatura = 25

    def efeito_bioma(self):
        if self.estacao =="inverno":
            self.organismo.hidratacao -= 20
            self.organismo.temperatura += 1
        
        elif self.estacao == "verão":
            self.organismo.hidratacao -= 40
            self.organismo.temperatura += 2

        else:
            self.organismo.hidratacao -= 30
            self.organismo.temperatura += 0.5
# ORGANISMO

class Organismo():
    def __init__(self, nome, idade, bioma):
        self.nome = nome
        self.idade = idade
        self.bioma = bioma
        self.hidratacao = 100
        self.temperatura = 36.5
        self.batimento = 85
        self.cerebro = Cerebro() 
        self.coracao = Coracao()

    def Escalar(self, altura):
 
        self.cerebro.oxigenacao_cerebro -= 10 * altura/3000
        self.bioma.efeito_bioma()

        if  self.oxigenacao_cerebro >= 95:
            print("ok!")
            print(self.cerebro.oxigenacao_cerebro())
 
        elif self.cerebro.oxigenacao_cerebro <= 94 and self.oxigenacao_cerebro >= 90:
            self.cerebro.diminuir_impulsos()
            print("!!CUIDADO!! HIPOXEMIA LEVE A MODERADA")
            print("SINTOMAS: Falta de ar / Tontura / Dificuldade para raciocinar ") 
            print(self.cerebro.oxigenacao_cerebro())
            
        elif self.cerebro.oxigenacao_cerebro <= 89 and self.oxigenacao_cerebro >= 85:
            
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            print("!!CUIDADO!! HIPOXEMIA SEVERA")
            print("SINTOMAS: Falta de ar intensa / Tontura forte / inicio de Cianose ")
            print(self.cerebro.oxigenacao_cerebro())
            
        elif self.cerebro.oxigenacao_cerebro <= 84 and self.oxigenacao_cerebro >= 80:
            
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            print("!!CUIDADO!! Os órgãos vitais (cérebro, rins e coração) começam a entrar em sofrimento por falta de oxigênio crônica. O cérebro começa a reduzir suas funções para poupar energia.")
            print("SINTOMAS: letargia, desorientação total no tempo e espaço, extrema dificuldade para falar ou se manter acordado, além de palidez extrema.")
            print(self.cerebro.oxigenacao_cerebro())
        
        elif self.cerebro.oxigenacao_cerebro <= 80 and self.oxigenacao_cerebro >= 71:
             
             self.cerebro.diminuir_impulsos()
             self.cerebro.diminuir_impulsos()
             self.cerebro.diminuir_impulsos()
             print("!!CUIDADO!! O cérebro corre risco iminente de sofrer lesões permanentes devido à falta prolongada de oxigenação.")
             print("Perda de consciência (desmaio/coma), convulsões e risco imediato de parada cardiorrespiratória.") 
             print(self.cerebro.oxigenacao_cerebro())
        else:
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            print("VocÊ tem 6 minutos até lesões irreversíveis nas células cerebrais")
            print("Você tem 10 minuros até sua morte, Boa sorte")
            print(self.cerebro.oxigenacao_cerebro())

    


# orgãos

class Coracao:
    def __init__(self):
        self.batimento = 90
    
    def aumentar_batimento(self):
            self.batimento += 50
    
    def diminuir_batimento(self):
            self.batimento -= 20



class Cerebro():
    def __init__(self):
        self.oxigenacao_cerebro = 100
        self.impulsos_nervosos = 30

    def aumentar_impulsos(self):
        self.impulsos_nervosos += 60

    def diminuir_impulsos(self):
        self.impulsos_nervosos -= 8

        # tem q ser certo os valores de acordo com oq fazem ou posso escolher valores dentro do quadro previsto
