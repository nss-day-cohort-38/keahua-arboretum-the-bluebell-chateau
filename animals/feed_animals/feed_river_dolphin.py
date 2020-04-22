import os
# from environments import River
from animals import RiverDolphin


def feed_river_dolphin():
    os.system('cls' if os.name == 'nt' else 'clear')

    dolphin = RiverDolphin()
    dolphin_prey = dolphin.prey
    feeding_time = sorted(list(dolphin_prey))

    for index, food in enumerate(feeding_time):
        print(f"{index + 1}. {food}")

    choice = input("\nWhat is on the menu for the River Dolphin today?\n >_ ")

    if choice == "1":
        dolphin.feed(feeding_time[int(choice) - 1])

    if choice == "2":
        dolphin.feed(feeding_time[int(choice) - 1])
        
    if choice == "3":
        dolphin.feed(feeding_time[int(choice) - 1])
        
    if choice == "4":
        dolphin.feed(feeding_time[int(choice) - 1])
        
    if choice == "5":
        dolphin.feed(feeding_time[int(choice) - 1])

    choice = input("\nPress any key to go back.\n >_")
    # if choice == "1":
    #     river = River()
    #     arboretum.rivers.append(river)
    # if choice == "2":
    #     pass

    # for index, river in enumerate(arboretum.rivers):
    # print(f'{index + 1}. River {river.id}')
