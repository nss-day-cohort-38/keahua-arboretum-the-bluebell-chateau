from environments import River
from environments import Mountain
from environments import Grassland

def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'River [{river.id}]')

    for mountain in arboretum.mountains:
        print(f'Mountain [{mountain.id}]')
    
    for grassland in arboretum.grasslands:
        print(f'Grassland [{grassland.id}]')

    input("\n\nPress any key to continue...")