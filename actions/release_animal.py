from animals import RiverDolphin
import os
from environments import River, Grassland, Forest, Coastline, Swamp, Mountain
from animals import Gecko, Nene_Goose, Kikakapu, Pueo, Ulae, Opeapea, HappyFaceSpider

# So it seems like what #2 should do is render the biomes that will take
# the animals depending on what animal is selected. The graph in README 
# shows eligible biomes for each animal. 

# And each biome should have animals array. So if animal is selected, print
# the eligible biome names, as well as the length of the animals arr for
# those biomes!

# Then a new input for which biome to append/add the animal choice to,
# with a nested if for when the len() of that arr is maxed out, print a 
# message with another input for a new choice.
def release_animal(arboretum):
    animal = None
    os.system('cls' if os.name == 'nt' else 'clear')

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("\nChoose animal. \n>_ ")

    if choice == "1":
        animal = Gecko()
        forest = Forest()

        print(f"\n1. Forest ({len(forest.animals)} animals)")

        biome_choice = input(f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1":
            forest.add_animal(animal)
            arboretum.annex_forest(forest)
            # TODO: Figure out why it's jumping back to main menu before
            # printing updated animals arr length
            print(f"\nForest ({len(forest.animals)} animals)")

    if choice == "2":
        animal = RiverDolphin()
        river = River()
        coastline = Coastline()

        print(f"\n1. River ({len(river.animals)} animals)")
        print(f"2. Coastline ({len(coastline.animals)} animals)")

        # SO weird. Once I added below line, broke the other animal choices
        # until I re-added the below line to all other choices.
        biome_choice = input(f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1":
            river.add_animal(animal)
            arboretum.annex_river(river)

            print(f"\nRiver ({len(river.animals)} animals)")

        elif biome_choice == "2":
            coastline.add_animal(animal)
            print(f"Coastline ({len(coastline.animals)} animals)")

    if choice == "3":
        animal = Nene_Goose()
        grassland = Grassland()

        print(f"\n1. Grassland ({len(grassland.animals)} animals)")

        biome_choice = input(f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1":
            grassland.add_animal(animal)
            arboretum.annex_grasslands(grassland)
            
            print(f"\nGrassland ({len(grassland.animals)} animals)")
            input("\nPress any key to return to the main menu \n>_")

    if choice == "4":
        animal = Kikakapu()
        river = River()
        swamp = Swamp()

        print(f"\n1. River ({len(river.animals)} animals)")
        print(f"2. Swamp ({len(swamp.animals)} animals)")

        biome_choice = input(f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1":
            river.add_animal(animal)
            print(f"\nRiver ({len(river.animals)} animals)")

        elif biome_choice == "2":
            swamp.add_animal(animal)
            print(f"Swamp ({len(swamp.animals)} animals)")

    if choice == "5":
        animal = Pueo()
        grassland = Grassland()
        forest = Forest()

        print(f"\n1. Grassland ({len(grassland.animals)} animals)")
        print(f"2. Forest ({len(forest.animals)} animals)")

        biome_choice = input(f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1":
            grassland.add_animal(animal)
            print(f"\nGrassland ({len(grassland.animals)} animals)")

        elif biome_choice == "2":
            forest.add_animal(animal)
            print(f"Forest ({len(forest.animals)} animals)")

    if choice == "6":
        animal = Ulae()
        coastline = Coastline()

        print(f"\n1. Coastline ({len(coastline.animals)} animals)")

        biome_choice = input(f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1":
            coastline.add_animal(animal)
            print(f"\nCoastline ({len(coastline.animals)} animals)")

    if choice == "7":
        animal = Opeapea()
        mountain = Mountain()
        forest = Forest()

        print(f"\n1. Mountain ({len(mountain.animals)} animals)")
        print(f"2. Forest ({len(forest.animals)} animals)")

        biome_choice = input(f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1":
            mountain.add_animal(animal)
            print(f"\nMountain ({len(mountain.animals)} animals)")

        elif biome_choice == "2":
            forest.add_animal(animal)
            print(f"Forest ({len(forest.animals)} animals)")

    if choice == "8":
        animal = HappyFaceSpider()
        swamp = Swamp()

        print(f"\n1. Swamp ({len(swamp.animals)} animals)")

        biome_choice = input(f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1":
            swamp.add_animal(animal)
            print(f"Swamp ({len(swamp.animals)} animals)")








# choice = input("\nChoose which biome to release the animal.\n>_ ")

    # def release_into_biome():
    # create list of biomes. loop through list to check if that biome is in the list. 
    # for environment in dir(aboretum):
    # if environment in biome_list:
    # for environment_instance in arboretum[environment]:
    # print(evironment_instance)

    # biome_list = ["Coastlines", "Rivers", "Forests", "Mountains", "Swamps", "Grasslands"]
    
    # biomes = []
    
    # for river in arboretum.rivers:
    #     biomes.append(river)
    
    # for environment in biome_list:
    #     if environment in dir(arboretum):
    #         for index, biome in enumerate(biome_list):
    #             print(f"{index + 1}. {biome}")
            # river_list = arboretum.rivers
            # for index, river in enumerate(river_list):
            #     print(f'{index + 1}. River {river.id}')
            #     print(environment)
                
    # choice = input("\nChoose which biome to release the animal.\n>_ ")

    

    # if choice == "5":
        # sorted_rivers.append(animal)
        # arboretum.rivers[int(choice) - 1].animals.append(animal)

    # choice = input("\n> ")

    # arboretum.mountain[int(choice) - 1].animals.append(animal)

    # arboretum.swamp[int(choice) - 1].animals.append(animal)

    # arboretum.grassland[int(choice) - 1].animals.append(animal)

    # arboretum.forest[int(choice) - 1].animals.append(animal)

    # arboretum.coastline[int(choice) - 1].animals.append(animal)

