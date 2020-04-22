import os
from environments import River

def feed_river_dolphin():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("1. Trout")
    print("2. Mackarel")
    print("3. Salmon")
    print("4. Sardine")

    choice = input("\nWhat is on the menu for the River Dolphin today?\n >_ ")

    # if choice == "1":
    #     river = River()
    #     arboretum.rivers.append(river)
    # if choice == "2":
    #     pass
