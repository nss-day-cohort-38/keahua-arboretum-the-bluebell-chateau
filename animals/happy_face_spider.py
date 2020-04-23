from animals import Animal
from interfaces import Identifiable

class HappyFaceSpider(Animal, Identifiable):

    def __init__(self):
        Animal.__init__(self, "Happy-Face Spider")
        Identifiable.__init__(self)
        self.__prey = { "fruit flies", "grasshoppers" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'\nThe happy-face spider ate {prey} for a meal')
        else:
            print(f'The happy-face spider rejects the {prey}')


    def __str__(self):
        return f'Happy-Face Spider {self.id}. I created spiderman!'
