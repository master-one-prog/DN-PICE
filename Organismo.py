
from Coracao import Coracao
from Cerebro import Cerebro

class Organismo():
    def __init__(self, nome, idade, bioma):
        self.nome = nome
        self.idade = idade
        self.bioma = bioma
        
        self.hidratacao = 100
        self.temperatura = 36.5
        self.cerebro = Cerebro() 
        self.coracao = Coracao()

    def efeitos_açao(self):
        if  self.cerebro.oxigenacao_cerebro >= 95:
                    print("")
                    print("ok!")
                    print("")
                    self.mostrar_status()
                    
        elif self.cerebro.oxigenacao_cerebro <= 94 and self.cerebro.oxigenacao_cerebro >= 90:
            self.cerebro.diminuir_impulsos()
            print("")
            print("!!CUIDADO!! HIPOXEMIA LEVE A MODERADA")
            print("SINTOMAS: Falta de ar / Tontura / Dificuldade para raciocinar ") 
            
            print("")
            self.mostrar_status()
            
        elif self.cerebro.oxigenacao_cerebro <= 89 and self.cerebro.oxigenacao_cerebro >= 85:
            
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            print("")
            print("!!CUIDADO!! HIPOXEMIA SEVERA")
            print("SINTOMAS: Falta de ar intensa / Tontura forte / inicio de Cianose ")
            
            print("")
            self.mostrar_status()
            
            
        elif self.cerebro.oxigenacao_cerebro <= 84 and self.cerebro.oxigenacao_cerebro >= 80:
            
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            print("")
            print("!!CUIDADO!! Os órgãos vitais (cérebro, rins e coração) começam a entrar em sofrimento por falta de oxigênio crônica. O cérebro começa a reduzir suas funções para poupar energia.")
            print("SINTOMAS: letargia, desorientação total no tempo e espaço, extrema dificuldade para falar ou se manter acordado, além de palidez extrema.")
            
            print("")
            self.mostrar_status()
        
        elif self.cerebro.oxigenacao_cerebro <= 80 and self.cerebro.oxigenacao_cerebro >= 71:
                
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            print("")
            print("!!CUIDADO!! O cérebro corre risco iminente de sofrer lesões permanentes devido à falta prolongada de oxigenação.")
            print("Perda de consciência (desmaio/coma), convulsões e risco imediato de parada cardiorrespiratória.") 
                
            print("")
            self.mostrar_status()
        else:
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            self.cerebro.diminuir_impulsos()
            print("")
            print("VocÊ tem 6 minutos até lesões irreversíveis nas células cerebrais")
            print("Você tem 10 minuros até sua morte, Boa sorte")
            
            print("")
            
            self.mostrar_status()

    def Escalar(self, altura):
 
        self.cerebro.oxigenacao_cerebro -= 10 * altura/3000
        self.bioma.organismo = self
        self.bioma.efeito_bioma()
        self.efeitos_açao()

        
    def Correr(self, distancia):
        self.cerebro.oxigenacao_cerebro -= 5 * distancia/3000
        self.bioma.organismo = self
        self.bioma.efeito_bioma()
        self.efeitos_açao()

    def Nadar(self, distancia):
        self.cerebro.oxigenacao_cerebro -= 9 * distancia/3000
        self.bioma.organismo = self
        self.bioma.efeito_bioma()
        self.efeitos_açao() 

    def Pular(self, forca_impulso):
        self.cerebro.oxigenacao_cerebro -= 7 * forca_impulso/3000
        self.bioma.organismo = self
        self.bioma.efeito_bioma()
        self.efeitos_açao()

    def mostrar_status(self):
        print(f"oxigenação do cérebro: {self.cerebro.oxigenacao_cerebro} ")
        print(f"hidratação : {self.hidratacao}")
        print(f"temperatura corporal: {self.temperatura}")
        print(f"batimento cardíaco: {self.coracao.batimento}")