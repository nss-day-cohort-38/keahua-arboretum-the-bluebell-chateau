import os
from environments import River
from environments import Mountain
from environments import Swamp
from environments import Grassland
from environments import Forest

def annex_biome(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("6. Coastline")

    choice = input("\nChoose what you want to annex.\n >_ ")

    if choice == "1":
        mountain = Mountain()
        arboretum.mountains.append(mountain)
    if choice == "2":
        swamp = Swamp()
        arboretum.swamps.append(swamp)
    if choice == "3":
        grassland = Grassland()
        arboretum.grasslands.append(grassland)
    if choice == "4":
        forest = Forest()
        arboretum.forests.append(forest)
    if choice == "5":
        river = River()
        arboretum.rivers.append(river)
    if choice == "6":
        coastline = Coastline()
        arboretum.coastlines.append(coastline)
