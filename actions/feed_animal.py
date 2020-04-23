import os
from arboretum import Arboretum
from .list_of_prey import feed_river_dolphin
from .list_of_prey import feed_gold_dust_day_gecko
from .list_of_prey import feed_opeapea

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

def food_menu():
  
    feed_animal()
    choice = input("\nChoose animal to feed.\n>_ ")

    if choice == "1":
        feed_gold_dust_day_gecko()

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

    if choice == "7":
        feed_opeapea()

    # if choice != "8":
    #     main_menu()
 