import os
from animals import Ulae


def feed_Ulae():
    os.system('cls' if os.name == 'nt' else 'clear')

    lizard_fish = Ulae()
    lizardfish_prey = lizard_fish.prey
    feeding_time = sorted(list(lizardfish_prey))

    for index, food in enumerate(feeding_time):
        print(f"{index + 1}. {food}")

    choice = input("\nWhat is on the menu for the River Dolphin today?\n >_ ")

    if choice == "1":
        lizard_fish.feed(feeding_time[int(choice) - 1])

    if choice == "2":
        lizard_fish.feed(feeding_time[int(choice) - 1])
        
    if choice == "3":
        lizard_fish.feed(feeding_time[int(choice) - 1])
        
    if choice == "4":
        lizard_fish.feed(feeding_time[int(choice) - 1])

    choice = input("\nPress any key to go back.\n >_")