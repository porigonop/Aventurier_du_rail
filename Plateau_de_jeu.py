#usr/bin/env python3
####################################
#Authors : Antoine L. et Lauren V. #
#Last Modification :01/25/2017     #
####################################
from Graph import Graph
from Wagon import Wagon
from CarteWagon import CarteWagon
from CarteDestination import CarteDestination
from Joueur import Joueur
class Plateau_de_jeu:
    """ """
    
    def __init__(self):
        """ """
        self.graph = graph
        self.pioche_wagon = pioche_wagon
        self.pioche_destination = pioche_destination
        self.carte_wagon = [pioche_wagon.pick() for i in range(5)]
        self.joueur_1 = Humain(pioche_wagon, pioche_destination, adversaire = None)
        self.joueur_2 = Humain(pioche_wagon, pioche_destiation, adversaire = self.joueur_1)
        self.joueur_1.adversaire = self.joueur_2

    def jouer(self):
        """ """
        
        joueur = self.joueur_1
        while True:
            joueur.jouer()
            if len(joueur.adversaire.reserve_de_wagon) <= 2:
                break
            joueur = joueur.adversaire
