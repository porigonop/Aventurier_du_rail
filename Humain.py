from Joueur import Joueur
from PiocheCarteDestination import PiocheCarteDestination
from PiocheCarteWagon import PiocheCarteWagon
from CarteDestination import CarteDestination

class Humain(Joueur):
    def jouer(self):
        print("le joueur " + self.color + " joue")
        print("il possédes les cartes wagons suivantes : ")
        for carte in self.carte_wagon:
            print(carte)
        
        print("il possédes les cartes destination : ")
        for carte in self.carte_destination:
            print(carte)
            print("--------")
        print("et il lui reste : " +\
         str(len(self.reserve_de_wagon)) \
         + " wagons")
         print("que voulez vous faire ?")
         
        
    def prendre_wagon(self):
        for i in range(2):
            print("les wagon visibles sont : ")
            for carte in plateau.visible:
                print(carte)
            
            print("idiquer une couleur si vous voulez prendre une carte visible sinon pressez entrer")
            answer = input()
            



if __name__ == "__main__":
    fh = open("fichiercsv/cartes_objectifs_-_version_epuree.csv")
    liste = [line[0:-1].split(":") for line in fh]
    liste.pop(0)
    #print(liste)
    carte_destination = [CarteDestination(dep, arr, val) for dep, arr, val in liste]
    pioche_d = PiocheCarteDestination(carte_destination)
    pioche_d.shuffle()
    pioche_w = PiocheCarteWagon()
    pioche_w.shuffle()
    j = Humain(pioche_w, pioche_d)
    j.jouer()
