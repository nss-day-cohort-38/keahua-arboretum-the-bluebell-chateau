import os
# from environments import River
from animals import Gecko


def feed_gold_dust_day_gecko():
    os.system('cls' if os.name == 'nt' else 'clear')

    gecko = Gecko()
    gecko_prey = gecko.prey
    feeding_time = sorted(list(gecko_prey))

    for index, food in enumerate(feeding_time):
        print(f"{index + 1}. {food}")

    choice = input("\nWhat is on the menu for the Gecko today?\n >_ ")

    if choice == "1":
        gecko.feed(feeding_time[int(choice) - 1])

    if choice == "2":
        gecko.feed(feeding_time[int(choice) - 1])
        
    if choice == "3":
        gecko.feed(feeding_time[int(choice) - 1])
        
    if choice == "4":
        gecko.feed(feeding_time[int(choice) - 1])

    choice = input("\nPress any key to go back.\n >_")
