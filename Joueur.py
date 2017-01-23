#usr/bin/env python3
from Wagon import Wagon
from CarteWagon import CarteWagon
from CarteDestination import CarteDestination

class Joueur:
    """ """
    color = ['bleu','rouge', 'vert', 'jaune', 'noir']
    index = 0
    def __init__(self, pioche_wagon, pioche_destination, adversaire = None):
        """ """
        self.color = Joueur.color[Joueur.index]
        Joueur.index += 1
        self.adversaire = adversaire
        self.score = 0
        self.carte_wagon = [pioche_wagon.pick() for i in range(4)]
        self.carte_destination = [pioche_destinatin.pick() for j in range(3)]
        self.reserve_de_wagon = [Wagon(self.color) for i in range(45)]


    def calculate_final_score(self):
        """ """
        pass
