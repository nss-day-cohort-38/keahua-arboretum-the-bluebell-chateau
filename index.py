import os
from arboretum import Arboretum
from actions.annex import annex_biome
from actions.release_animal import release_animal
from actions.report import build_facility_report
from actions.feed_animal import food_menu

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print("|  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |")
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+\n")
    print("1. Annex Biome")
    print("2. Release New Animal")
    print("3. Feed Animal")
    print("4. Cultivate New Plant")
    print("5. Show Arboretum Report")
    print("6. Exit\n")
    print("Choose a KILLER option.")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input(">_ ")

    if choice == "1":
        annex_biome(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        food_menu()
        # keahua
    if choice == "4":
        pass

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()

main_menu()
