from environments import River
from environments import Mountain
from environments import Grassland
from environments import Forest
from environments import Swamp
from environments import Coastline

def build_facility_report(arboretum):
    for river in arboretum.rivers:
        river_id = str(river.id)
        river_list = list(river_id)
        sliced_river = river_list[:8]
        river_animals = river.animals
        print(f'River [{"".join(sliced_river)}]')
        
        for animal in river_animals:
            animal_id = str(animal.id)
            animal_id_list = list(animal_id)
            sliced_animal_id = animal_id_list[:8]
            print(f'\t{animal.species} ({"".join(sliced_animal_id)})')

    for mountain in arboretum.mountains:
        mountain_id = str(mountain.id)
        mountain_list = list(mountain_id)
        sliced_mountain = mountain_list[:8]
        mountain_animals = mountain.animals
        print(f'Mountain [{"".join(sliced_mountain)}]')

        for animal in mountain_animals:
            animal_id = str(animal.id)
            animal_id_list = list(animal_id)
            sliced_animal_id = animal_id_list[:8]
            print(f'\t{animal.species} ({"".join(sliced_animal_id)})')
    
    for grassland in arboretum.grasslands:
        grassland_id = str(grassland.id)
        grassland_list = list(grassland_id)
        sliced_grassland = grassland_list[:8]
        grassland_animals = grassland.animal
        print(f'Grassland [{"".join(sliced_grassland)}]')
        
        for animal in grassland_animals:
            animal_id = str(animal.id)
            animal_id_list = list(animal_id)
            sliced_animal_id = animal_id_list[:8]
            print(f'\t{animal.species} ({"".join(sliced_animal_id)})')


    for forest in arboretum.forests:
        forest_id = str(forest.id)
        forest_list = list(forest_id)
        sliced_forest = forest_list[:8]
        forest_animals = forest.animals
        print(f'\nForest [{"".join(sliced_forest)}]')

        for animal in forest_animals:
            animal_id = str(animal.id)
            animal_id_list = list(animal_id)
            sliced_animal_id = animal_id_list[:8]
            print(f'\t{animal.species} ({"".join(sliced_animal_id)})')

    for swamp in arboretum.swamps:
        swamp_id = str(swamp.id)
        swamp_list = list(swamp_id)
        sliced_swamp = swamp_list[:8]
        swamp_animals = swamp.animals
        print(f'Swamp [{"".join(sliced_swamp)}]')

        for animal in swamp_animals:
            animal_id = str(animal.id)
            animal_id_list = list(animal_id)
            sliced_animal_id = animal_id_list[:8]
            print(f'\t{animal.species} ({"".join(sliced_animal_id)})')

    for coastline in arboretum.coastlines:
        coastline_id = str(coastline.id)
        coastline_list = list(coastline_id)
        sliced_coastline = coastline_list[:8]
        coastline_animals = coastline.animals
        print(f'\ncoastline [{"".join(sliced_coastline)}]')

        for animal in coastline_animals:
            animal_id = str(animal.id)
            animal_id_list = list(animal_id)
            sliced_animal_id = animal_id_list[:8]
            print(f'\t{animal.species} ({"".join(sliced_animal_id)})')

    input("\n\nPress any key to continue...")