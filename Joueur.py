"""
contient le joueur
"""
from Wagon import Wagon


class Joueur:
    """
    defini les attributs d'un joueur
    """
    color = ['Bleu', 'Rouge', 'Vert', 'Jaune', 'Noir']
    index = 0
    def __init__(self, pioche_wagon, pioche_destination, adversaire=None):
        """
        crée le joueur
        """
        self.color = Joueur.color[Joueur.index]
        Joueur.index += 1
        self.adversaire = adversaire
        self.score = 0
        self.carte_wagon = [pioche_wagon.pick() for i in range(25)]
        self.carte_destination = [pioche_destination.pick() \
                                    for j in range(1)]
        self.reserve_de_wagon = [Wagon(self.color) for i in range(45)]


    def calculate_final_score(self):
        """
        permet de connaitre le score final du joueur
        """
        pass
