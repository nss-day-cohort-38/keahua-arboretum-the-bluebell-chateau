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

    # Will print a menu of biomes with conditionals to add the selected
    # biome to keahua's array for that biome.
    if choice == "1":
        annex_biome(keahua)

    # Will print list of animals to release to a biome. Conditionals based
    # on animal selected to print the biomes for that animal, and the len()
    # of the animals arr for those biomes to make sure there's room.
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
