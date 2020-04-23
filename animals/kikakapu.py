from animals import Animal
from interfaces import Identifiable
from interfaces import ISwimming
from interfaces import IAquatic
from interfaces import ISaltwater

class Kikakapu(Animal, ISwimming, ISaltwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Kikakapau")
        ISwimming.__init__(self)
        IAquatic.__init__(self)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'\nThe Kikakapau ate {prey} for a meal')
        else:
            print(f'The Kikakapau rejects the {prey}')


    def __str__(self):
        return f'Kikakapau {self.id}. does not speak'