from Joueur import Joueur
from PiocheCarteDestination import PiocheCarteDestination
from PiocheCarteWagon import PiocheCarteWagon
from CarteDestination import CarteDestination
from CarteWagon import CarteWagon
class Humain(Joueur):
    def jouer(self, plateau):
        
        print("le joueur " + self.color + " joue")
        
        print("il possédes les cartes wagons suivantes : ")
        for carte in self.carte_wagon:
            print(carte)
        """
        print("il possédes les cartes destination : ")
        for carte in self.carte_destination:
            print(carte)
            print("--------")
        print("et il lui reste : " +\
         str(len(self.reserve_de_wagon)) \
         + " wagons")
        #print("enfin le plateau est : ")
        #print("--------------------------")
        #print(plateau.graph)
        """
        print("que voulez vous faire ?\n"+\
        "prendre wagon\n" + \
        "prendre destination")
        while True:
            answer = input()
            if answer == "prendre wagon":
                self.prendre_wagon(plateau)
                return True
            elif answer == "prendre destination":
                self.prendre_destination(plateau)
                return True
            elif answer == "":#"poser route":
                self.poser_route(plateau)
                return True
    def prendre_wagon(self, plateau):
        print("les wagons visibles sont : ")
        for carte in plateau.visible:
            print(carte)
            
        while True:
            print("indiquer une couleur si vous voulez prendre une carte visible sinon pressez entrer")
            answer = input()
            if answer == "":
                carte = plateau.pioche_wagon.pick()
                self.carte_wagon.append(carte)
                print("vous piocher une " + str(carte))
                break
            else:
                try:
                    answer = int(answer)
                except:
                    pass
                if answer in range(5):
                    print("vous jouez")
                    
                    carte = plateau.visible.pop(answer)
                    self.carte_wagon.append(carte)
                    plateau.visible.append(plateau.pioche_wagon.pick())
                    print("vous piocher une " + str(carte))
                    if carte.color == "multicolor":
                        return
                    break
            print("couleur non trouvée")
            
        print("les wagon visibles sont : ")
        for carte in plateau.visible:
            print(carte)
            
        while True:
            print("indiquer une couleur si vous voulez prendre une carte visible sinon pressez entrer")
            answer = input()
            if answer == "":
                carte = plateau.pioche_wagon.pick()
                self.carte_wagon.append(carte)
                
                print("vous piocher une " + str(carte))
                break
            else:
                try:
                    answer = int(answer)
                except:
                    pass
                if answer in range(5):
                    carte = plateau.visible.pop(answer)
                    if carte.color == "multicolor":
                        plateau.visible.append(carte)
                        continue
                    self.carte_wagon.append(carte)
                    plateau.visible.append(plateau.pioche_wagon.pick())
                    print("vous piocher une " + str(carte))
                    break
            print("couleur non trouvée")

    def prendre_destination(self, plateau):
        lst = []
        for i in range(3):
            try:
                lst.append(plateau.pioche_destination.pick())
            except:
                print("il n'y avait pas assez de cartes")
                break
        print("voici vos cartes destination")
        for carte in lst:
            print(carte)
            print("----------------")
        impo = True
        while impo:
            print("choississez les cartes voulu en indiquant leur positions, séparé d'un éspace")
            answer = input()
            answer = sorted(answer.split(" "))
            answer.reverse()
            impo = False
            for elt in answer:
                if int(elt) >= len(lst):
                    print("impo")
                    impo = True
            if impo:
                continue
                
            for i in answer:
                i = int(i)
                self.carte_destination.append(lst.pop(i))
            for carte in lst:
                plateau.pioche_destination.pioche.append(carte)
            
    def poser_route(self, plateau):
        while True:
            depart = input("ville de départ : ")
            
            if not depart in plateau.graph.nodes:
                print("mauvais nom de ville")
                continue
            
            arriver = input("ville d'arriver : ")
            
            if depart == arriver or not arriver in plateau.graph.nodes:
                print("mauvais nom de ville")
                continue
            
            if not depart in plateau.graph.adjacency_list[arriver] and (depart, arriver) in plateau.used:
                print("la route n'est pas disponible")
                break
            
            for edge in plateau.graph.edges:
                if edge[0] == depart and edge[1] == arriver:
                    if not len(self.reserve_de_wagon) < edge[2]:
                        print("pas assez de wagons")
                        pass
                    else:
                        cartes = [carte for carte in self.carte_wagon if carte.color == edge[3]]
                        if len(cartes) < edge[2]:
                            print("pas assez de carte :", cartes, edges[2])
                            pass
                        else:
                            print("oui !")
                            plateau.used.append((depart, arriver))
                            plateau.used.append((arriver, depart))
                            plateau.uscol.append(self.color)
                            return True
            
        
        
