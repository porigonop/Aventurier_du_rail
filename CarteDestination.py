#usr/bin/env python3


class CarteDestination:
    """ """

    def __init__(self, departure, arrival):
        """ """
        self.departure = departure
        self.arrival = arrival


    def __repr__(self):
        """ """
        return 'Point de départ ---> ' + self.departure + ' \n'
               ' Point d''arrivée ---> ' + self.arrival
