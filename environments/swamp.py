import sys
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
sys.path.append('../')

# from environments.environment import Environment
# from interfaces.biome import IStagnant
# from animals.


class Swamp(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      # self.name = name
      self.inhabitants = []
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
  
    def animal_count(self):
        return "This place has a bunch of animals in it"

    def add_animal(self, animal):
        try:
          self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Error!")

    def add_plant(self, plant):
        try:
          self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Error!")
    def __str__(self):
        print("swamp object")
    # def addInhabitant(self, item):
    #     if not isinstance(item, IStagnant):
    #         raise TypeError(f"{item} is not of type IStagnant")
    #     self.inhabitants.append(item)

    # def __str__(self):
    #     return self.name