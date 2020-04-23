import os
# from environments import River
from animals import Pueo


def feed_pueo():
    os.system('cls' if os.name == 'nt' else 'clear')

    pueo = Pueo()
    pueo_prey = pueo.prey
    feeding_time = sorted(list(pueo_prey))

    for index, food in enumerate(feeding_time):
        print(f"{index + 1}. {food}")

    choice = input("\nWhat is on the menu for the Pueo today?\n >_ ")

    if choice == "1":
        pueo.feed(feeding_time[int(choice) - 1])

    if choice == "2":
        pueo.feed(feeding_time[int(choice) - 1])
        
    if choice == "3":
        pueo.feed(feeding_time[int(choice) - 1])
        
    if choice == "4":
        pueo.feed(feeding_time[int(choice) - 1])

    choice = input("\nPress any key to go back.\n >_")
