from animals import RiverDolphin
import os
from environments import River
from animals import Gecko, Nene_Goose, Kikakapu, Pueo, Ulae, Opeapea, HappyFaceSpider


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

    if choice == "2":
        animal = RiverDolphin()

    if choice == "3":
        animal = Nene_Goose()

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        animal = Pueo()

    if choice == "6":
        animal = Ulae()

    if choice == "7":
        animal = Opeapea()

    if choice == "8":
        animal = HappyFaceSpider()


    # def release_into_biome():
    # create list of biomes. loop through list to check if that biome is in the list. 
    # for environment in dir(aboretum):
    # if environment in biome_list:
    # for environment_instance in arboretum[environment]:
    # print(evironment_instance)

    biome_list = ["Coastlines", "Rivers", "Forests", "Mountains", "Swamps", "Grasslands"]
    
    biomes = []
    
    for river in arboretum.rivers:
        biomes.append(river)
    
    for environment in biome_list:
        if environment in dir(arboretum):
            for index, biome in enumerate(biome_list):
                print(f"{index + 1}. {biome}")
            # river_list = arboretum.rivers
            # for index, river in enumerate(river_list):
            #     print(f'{index + 1}. River {river.id}')
            #     print(environment)
                
    choice = input("\nChoose which biome to release the animal.\n>_ ")

    if choice == "5":
        # sorted_rivers.append(animal)
        arboretum.rivers[int(choice) - 1].animals.append(animal)

    # choice = input("\n> ")

    # arboretum.mountain[int(choice) - 1].animals.append(animal)

    # arboretum.swamp[int(choice) - 1].animals.append(animal)

    # arboretum.grassland[int(choice) - 1].animals.append(animal)

    # arboretum.forest[int(choice) - 1].animals.append(animal)

    # arboretum.coastline[int(choice) - 1].animals.append(animal)

