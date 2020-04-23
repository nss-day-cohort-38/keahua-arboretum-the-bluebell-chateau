import os
from animals import Nene_Goose


def feed_nene_goose():
    os.system('cls' if os.name == 'nt' else 'clear')

    nene_goose = Nene_Goose()
    nene_goose_prey = nene_goose.prey
    feeding_time = sorted(list(nene_goose_prey))

    for index, food in enumerate(feeding_time):
        print(f"{index + 1}. {food}")

    choice = input("\nWhat is on the menu for the Nene Goose today?\n >_ ")

    if choice == "1":
        nene_goose.feed(feeding_time[int(choice) - 1])

    if choice == "2":
        nene_goose.feed(feeding_time[int(choice) - 1])
        
    if choice == "3":
        nene_goose.feed(feeding_time[int(choice) - 1])
        
    if choice == "4":
        nene_goose.feed(feeding_time[int(choice) - 1])

    choice = input("\nPress any key to go back.\n >_")