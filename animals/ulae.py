from animals import Animal
from interfaces import ISwimming
from interfaces import ISaltwater 
from interfaces import Identifiable

class Ulae(Animal, ISwimming, ISaltwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Ulae")
        ISwimming.__init__(self)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Shrimp", "Butterfly Fish", "Yellow Tang", "Goatfish" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'\nThe Ulae ate {prey} for a meal')
        else:
            print(f'The Ulae rejects the {prey}')


    def __str__(self):
        return f'Ulae {self.id}. Glub glub'