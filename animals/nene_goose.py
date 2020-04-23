from animals import Animal
from interfaces import ITerrestrial
from interfaces import IWalking
from interfaces import Identifiable
from interfaces import ISwimming

class Nene_Goose(Animal, ITerrestrial, IWalking, ISwimming, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        ITerrestrial.__init__(self)
        IWalking.__init__(self)
        ISwimming.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "seeds", "fruits", "nuts", "leaves" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'\nThe Nene Goose ate {prey} for a meal')
        else:
            print(f'The Nene Goose rejects the {prey}')


    def __str__(self):
        return f'Nene Goose {self.id}. does not speak'