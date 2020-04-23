from animals import Animal
from interfaces import ITerrestrial
from interfaces import IFlying
from interfaces import Identifiable

class Opeapea(Animal, ITerrestrial, IFlying, Identifiable):

    def __init__(self):
        Animal.__init__(self, "'Ope'Ape'a")
        ITerrestrial.__init__(self)
        IFlying.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "insects", "moths", "beetles", "termites" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, food):
        if food in self.__prey:
            print(f'\nThe \'Ope\'Ape\'a ate {food} for a meal')
        else:
            print(f'The \'Ope\'Ape\'a rejects the {food}')


    def __str__(self):
        return f'\'Ope\'Ape\'a {self.id}. does not speak'