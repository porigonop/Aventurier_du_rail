
####################################
#Authors : Antoine L. et Lauren V. #
#Last Modification :01/25/2017     #
####################################
from graphTrans import GraphTrans
from Graph import Graph
from CarteDestination import CarteDestination
from Humain import Humain
from Ordinateur import Ordinateur
from PiocheCarteDestination import PiocheCarteDestination
from PiocheCarteWagon import PiocheCarteWagon
from pprint import pprint


class PlateauDeJeu:
    """
    Class that define the board game
    """

    def __init__(self):
        """ Class constructor  of class PlateauDeJeu"""
        fileh = open("fichiercsv/cartes_objectifs_-_version_epuree.csv", encoding="UTF-8")
        liste = [line[0:-1].split(":") for line in fileh] 
        liste.pop(0)
        fileh.close()
        self.used = []   # liste de toutes les arêtes qi ont été
        self.uscol = []   # liste des couleurs utilisées pour les arêtes
        self.values_uscol = [] #liste de taille de l'arête utilisée et sa couleur 
        self.edgecolor = {}    # dico prend key en arete et en value la couleur du joueur
        self.graph = Graph()
        self.pioche_wagon = PiocheCarteWagon()
        self.pioche_wagon.shuffle()
        self.pioche_destination = PiocheCarteDestination([CarteDestination(dep, arr, val)\
                                                         for dep, arr, val in liste])

        self.pioche_destination.shuffle()
        self.visible = [self.pioche_wagon.pick() for i in range(5)]
        self.joueur_1 = Ordinateur(self.pioche_wagon, self.pioche_destination, adversaire=None)#Humain(self.pioche_wagon, self.pioche_destination, adversaire=None)
        self.joueur_2 = Ordinateur(self.pioche_wagon, self.pioche_destination, adversaire=self.joueur_1)#Humain(self.pioche_wagon, self.pioche_destination, adversaire=self.joueur_1)
        self.joueur_1.adversaire = self.joueur_2
        fileh = open("fichiercsv/cartes_bretagne_-_version_epuree.csv", encoding="UTF-8")
        lines = [line[:-1].split(":") for line in fileh][1:]
        fileh.close()
        for line in lines:
            if not line[0] in self.graph.nodes:
                self.graph.add_a_node(line[0])
            if not line[1] in self.graph.nodes:
                self.graph.add_a_node(line[1])
            self.graph.add_an_edge(line[0], line[1], int(line[2]), line[3])

        for edge in self.graph.edges:
            self.edgecolor[str(edge)] = None

    def jouer(self):
        """
        method that allows to play
        """
        joueur = self.joueur_1
        while True:
            joueur.jouer(self)
            if len(joueur.adversaire.reserve_de_wagon) <= 2:
                break
            joueur = joueur.adversaire
        print("joueur 1 :", self.joueur_1.calculate_final_score(self))
        print("joueur 2 :", self.joueur_2.calculate_final_score(self))
    def linked(self, depart, arrivee, color):
        new_g = GraphTrans()
        for node in self.graph.nodes:
            new_g.add_a_node(node)
        for edge in self.graph.edges:
            if self.edgecolor[str(edge)] == color:
                new_g.add_an_edge(edge[0], edge[1])
        new_gtrans = new_g.transitive_closure_V1()
        if (depart, arrivee) in new_gtrans.edges:
            return True
        else:
            return False

    
if __name__ == "__main__":
    PLATEAU = PlateauDeJeu()
    PLATEAU.jouer()
