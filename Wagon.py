"""
contient l'ogjet wagon
"""
class Wagon:
    """
    defini l'ogjet wagon
    """
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color
