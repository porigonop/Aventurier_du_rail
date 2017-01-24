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
from Humain import Humain
from PiocheCarteDestination import PiocheCarteDestination
from PiocheCarteWagon import PiocheCarteWagon
class Plateau_de_jeu:
    """ """
    
    def __init__(self):
        """ """
        fh = open("fichiercsv/cartes_objectifs_-_version_epuree.csv")
        liste = [line[0:-1].split(":") for line in fh]
        liste.pop(0)
        self.used = []
        self.uscol = []
        self.graph = Graph()
        self.pioche_wagon = PiocheCarteWagon()
        self.pioche_wagon.shuffle()
        self.pioche_destination = PiocheCarteDestination([CarteDestination(dep, arr, val) for dep, arr, val in liste])
        self.pioche_destination.shuffle()
        
        self.visible = [self.pioche_wagon.pick() for i in range(5)]
        self.joueur_1 = Humain(self.pioche_wagon, self.pioche_destination, adversaire = None)
        self.joueur_2 = Humain(self.pioche_wagon, self.pioche_destination, adversaire = self.joueur_1)
        self.joueur_1.adversaire = self.joueur_2
        
        fh = open("fichiercsv/cartes_bretagne_-_version_epuree.csv")
        lines = [line[:-1].split(":") for line in fh][1:]
        fh.close()
        for line in lines:
            if not line[0] in self.graph.nodes:
                self.graph.add_a_node(line[0])
            if not line[1] in self.graph.nodes:
                self.graph.add_a_node(line[1])
            self.graph.add_an_edge(line[0], line[1], int(line[2]), line[3])
        
    def jouer(self):
        """ """
        joueur = self.joueur_1
        while True:
            joueur.jouer(plateau)
            if len(joueur.adversaire.reserve_de_wagon) <= 2:
                break
            joueur = joueur.adversaire

if __name__ == "__main__":
    plateau = Plateau_de_jeu()
    plateau.jouer()
