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

        for index, forest in enumerate(arboretum.forests):
            print(f"\n {index + 1}. {forest} ({len(forest.animals)} animals)")

        biome_choice = input(
            f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1" and len(arboretum.forests[0].animals) < 20:

            arboretum.forests[0].add_animal(animal)
            input("\nPress any key to return to the main menu \n>_")

        if biome_choice == "2" and len(arboretum.forests[1].animals) < 20:

            arboretum.forests[1].add_animal(animal)

            input("\nPress any key to return to the main menu \n>_")

        if biome_choice == "3" and len(arboretum.forests[2].animals) < 20:

            if choice == "3":
                animal = Nene_Goose()
         
        for index, grassland in enumerate(arboretum.grasslands):
            print(f"\n {index + 1}. {grassland} ({len(grassland.animals)} animals)")
            arboretum.forests[2].add_animal(animal)

            input("\nPress any key to return to the main menu \n>_")

        if biome_choice == "1" and len(arboretum.grasslands[0].animals) < 21:
            arboretum.grasslands[0].add_animal(animal)
            input("\nPress any key to return to the main menu \n>_")

    if choice == "4":
        animal = Kikakapu()
        
        for index, swamp in enumerate(arboretum.swamps):
            print(f"\n {index + 1}. {swamp} ({len(swamp.animals)} animals)")
    
        biome_choice = input(f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1" and len(arboretum.swamps[0].animals) < 21:
            arboretum.swamps[0].add_animal(animal)
        if biome_choice == "4" and len(arboretum.forests[3].animals) < 20:

            arboretum.forests[3].add_animal(animal)

            input("\nPress any key to return to the main menu \n>_")

    if choice == "2":
        animal = RiverDolphin()

        for index, river in enumerate(arboretum.rivers):
            print(f"{index + 1}. {river} ({len(river.animals)} animals)")
            
        biome_choice = input(
            f"\nChoose which biome to release the {animal.species}.\n>_ ")

        if biome_choice == "1" and len(arboretum.rivers[0].animals) < 12:
            
            arboretum.rivers[0].add_animal(animal)
            input("\nPress any key to return to the main menu \n>_")
            
        if biome_choice == "2" and len(arboretum.rivers[1].animals) < 12:

            arboretum.rivers[1].add_animal(animal)
            input("\nPress any key to return to the main menu \n>_")
            
        if biome_choice == "3" and len(arboretum.rivers[2].animals) < 12:

            arboretum.rivers[2].add_animal(animal)
            input("\nPress any key to return to the main menu \n>_")
            
        if biome_choice == "4" and len(arboretum.rivers[3].animals) < 12:

            arboretum.rivers[3].add_animal(animal)
            input("\nPress any key to return to the main menu \n>_")

    if choice == "5":
        animal = Pueo()

        for index, forest in enumerate(arboretum.forests): 
            print(f"\n {index + 1}. {forest} ({len(forest.animals)} animals)")

        biome_choice = input(f"\nChoose which biome to release the {animal.species}.\n>_ ")


        if biome_choice == "1" and len(arboretum.forests[0].animals) < 20:
            arboretum.forests[0].add_animal(animal)
            input("\nPress any key to return to the main menu \n>_")

    if choice == "6":
        animal = Ulae()

        biome_choice = input(
            f"\nChoose which biome to release the {animal.species}.\n>_ ")

    if choice == "7":
        animal = Opeapea()

        biome_choice = input(
            f"\nChoose which biome to release the {animal.species}.\n>_ ")

    if choice == "8":
        animal = HappyFaceSpider()

        biome_choice = input(
            f"\nChoose which biome to release the {animal.species}.\n>_ ")

