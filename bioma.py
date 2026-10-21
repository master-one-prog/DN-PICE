
from abc import ABC, abstractmethod
import random
# BIOMAS 


class bioma(ABC):
    def __init__(self, estacao, nome):
        self.nome = nome
        self.estacao = estacao

    @abstractmethod
    def efeito_bioma(self):
        pass    

class Tundra(bioma):
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
            self.organismo.coracao.batimento += 15
            self.organismo.temperatura -= 2
        
        elif self.estacao == "verão":
            self.organismo.coracao.batimento += 10
            self.organismo.temperatura -= 1

        else:
            self.organismo.coracao.batimento += 7
            self.organismo.temperatura -= 0.5


    


class Floresta_Temperada(bioma):
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
            
        

class Deserto(bioma):
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



