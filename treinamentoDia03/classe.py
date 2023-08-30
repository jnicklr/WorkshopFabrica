from abc import ABC, abstractmethod


class IAnimal(ABC):
    
    @abstractmethod
    def falar(self):
        """defina na classe filha"""
        
    @abstractmethod
    def andar(self):
        """defina na classe filha"""
        
        
class Cachorro(IAnimal):
    
    def falar(self):
        print("Au Au!")
        
    def andar(self):
        print("Ando com 4 patas!")
        

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__humano = True
    
    def falar_pessoa(self):
        print("Falando!")
        
        

pingo = Cachorro()
pingo.falar()
pessoa = Pessoa("João", 18)
pessoa.falar_pessoa()