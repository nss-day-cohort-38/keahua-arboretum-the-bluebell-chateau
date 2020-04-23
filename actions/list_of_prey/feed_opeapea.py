import os
# from environments import River
from animals import Opeapea


def feed_opeapea():
    os.system('cls' if os.name == 'nt' else 'clear')

    opeapea = Opeapea()
    opeapea_prey = opeapea.prey
    feeding_time = sorted(list(opeapea_prey))

    for index, food in enumerate(feeding_time):
        print(f"{index + 1}. {food}")

    choice = input("\nWhat is on the menu for the \'Ope\'Ape\'a today?\n >_ ")

    if choice == "1":
        opeapea.feed(feeding_time[int(choice) - 1])

    if choice == "2":
        opeapea.feed(feeding_time[int(choice) - 1])
        
    if choice == "3":
        opeapea.feed(feeding_time[int(choice) - 1])
        
    if choice == "4":
        opeapea.feed(feeding_time[int(choice) - 1])

    choice = input("\nPress any key to go back.\n >_")
