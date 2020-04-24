from .plant import Plant

class Bluejayed_vine(Plant):
    def __init__(self):
        super().__init__()
        self.insecticide_resistance = "Medium"
        self.location = ["Grassland", "Swamp"]
        self.seeds_produced = 0
        self.sunlight = "Heavy"