from animals import Animal
from interfaces import IFlying
from interfaces import Identifiable

class Pueo(Animal, IFlying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Pueo")
        IFlying.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "mice", "rats", "squirrels", "kittens" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'\nThe Pueo ate {prey} for a meal')
        else:
            print(f'The Pueo rejects the {prey}')


    def __str__(self):
        return f'Pueo {self.id}. said "WHO WHO..."'