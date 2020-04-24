from animals import RiverDolphin
import os
from animals import Gecko, Nene_Goose, Kikakapu, Pueo, Ulae, Opeapea, HappyFaceSpider
from arboretum import Arboretum

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


    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river.id}')

    # print("Release the animal into which biome?\n")
    # print("1. Mountain")
    # print("2. Swamp")
    # print("3. Grassland")
    # print("4. Forest")
    # print("5. River")
    # print("6. Coastline")

    choice = input("\n> ")

    arboretum.rivers[int(choice) - 1].animals.append(animal)

    arboretum.mountain[int(choice) - 1].animals.append(animal)

    arboretum.swamp[int(choice) - 1].animals.append(animal)

    arboretum.grassland[int(choice) - 1].animals.append(animal)

    arboretum.forest[int(choice) - 1].animals.append(animal)

    arboretum.coastline[int(choice) - 1].animals.append(animal)



