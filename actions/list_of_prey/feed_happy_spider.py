import os
# from environments import River
from animals import HappyFaceSpider


def feed_happy_face_spider():
    os.system('cls' if os.name == 'nt' else 'clear')

    happyFaceSpider = HappyFaceSpider()
    happyFaceSpider_prey = happyFaceSpider.prey
    feeding_time = sorted(list(happyFaceSpider_prey))

    for index, food in enumerate(feeding_time):
        print(f"{index + 1}. {food}")

    choice = input("\nWhat is on the menu for the Happy-Face Spider today?\n >_ ")

    if choice == "1":
        happyFaceSpider.feed(feeding_time[int(choice) - 1])

    if choice == "2":
        happyFaceSpider.feed(feeding_time[int(choice) - 1])

    choice = input("\nPress any key to go back.\n >_")
