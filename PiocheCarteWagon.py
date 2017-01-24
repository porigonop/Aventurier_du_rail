from pprint import pprint
from CarteWagon import CarteWagon
import random
COLOR = ["Bleu", "Rose", "Orange", "Blanc",\
 "Vert", "Jaune", "Noir", "Rouge", "multicolor"]


class PiocheCarteWagon:
    def __init__(self):
        self.pioche = [CarteWagon(COLOR[i]) \
                        for i in range(len(COLOR)-1)\
                        for j in range(12)]+\
                        [CarteWagon(COLOR[-1]) for i in range(14)]
                        
        self.defausse = []
        
        
    def shuffle(self):
        random.shuffle(self.pioche)
    
    def pick(self):
        return self.pioche.pop()
    
    def defausse(self, carte):
        self.defausse.append(carte)
    
    def __repr__(self):
        return str(self.pioche)
    
if __name__ == "__main__":
    P = PiocheCarteWagon()
    P.shuffle()
    print(P.pick())
    
    salut = [i for i in range(10)]
    print(salut)
    print(salut.pop())
    print(salut)
