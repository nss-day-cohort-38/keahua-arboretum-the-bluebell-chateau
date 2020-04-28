from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Coastline(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)

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
        return(f"Coastline [{str(self.id)[:8]}]")
