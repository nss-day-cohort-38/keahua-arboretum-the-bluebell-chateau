import os
from animals import Kikakapu


def feed_kikakapu():
    os.system('cls' if os.name == 'nt' else 'clear')

    kikakapu = Kikakapu()
    kikakapu_prey = kikakapu.prey
    feeding_time = sorted(list(kikakapu_prey))

    for index, food in enumerate(feeding_time):
        print(f"{index + 1}. {food}")

    choice = input("\nWhat is on the menu for the Kikakapu today?\n >_ ")

    if choice == "1":
        kikakapu.feed(feeding_time[int(choice) - 1])

    if choice == "2":
        kikakapu.feed(feeding_time[int(choice) - 1])
        
    if choice == "3":
        kikakapu.feed(feeding_time[int(choice) - 1])
        
    if choice == "4":
        kikakapu.feed(feeding_time[int(choice) - 1])

    choice = input("\nPress any key to go back.\n >_")