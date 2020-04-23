from environments import River
from environments import Mountain


def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'River [{river.id}]')

    for mountain in arboretum.mountains:
        print(f'Mountain [{mountain.id}]')

    input("\n\nPress any key to continue...")