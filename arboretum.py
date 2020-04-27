class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rivers = []
        self.grasslands = []
        self.coastlines = []
        self.mountains = []
        self.swamps = []
        self.forests = []

    def annex_rivers(self, river):
        self.rivers.append(river)
    
    def annex_grasslands(self, grassland):
        self.grasslands.append(grassland)
    
    def annex_coastlines(self, coastline):
        self.coastlines.append(coastline)
    
    def annex_mountains(self, mountain):
        self.mountains.append(mountain)
    
    def annex_swamps(self, swamp):
        self.swamps.append(swamp)
    
    def annex_forests(self, forest):
        self.forests.append(forest)
        
        # convert to a dictionary in order to loop through values

# class Arboretum:

#     def __init__(self):
#         self.__rivers = []

#     @property
#     def rivers(self):
#         return self.__rivers

#     def annex_river(self, river):
#         self.__rivers.append(river)        
