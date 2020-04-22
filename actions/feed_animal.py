import os
from animals.feed_animals import feed_river_dolphin

def feed_animal():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("\nChoose animal to feed. \n>_ ")

def food_menu():
  
    feed_animal()
    choice = input(">_ ")

    if choice == "1":
        pass

    if choice == "2":
        feed_river_dolphin()

    # if choice == "3":
    #     feed_animal(keahua)

    # if choice == "4":
    #     pass

    # if choice == "5":
    #     build_facility_report(keahua)
    #     pass

    # if choice != "6":
    #     main_menu()

    # if choice != "7":
    #     main_menu()

    # if choice != "8":
    #     main_menu()

food_menu()
 