import requests
import json

def herb_location(year, species):
    base_url = 'https://api.gbif.org/v1/'
    search_url = 'occurrence/search'
    params = {'country': 'RU', 'year': year, 'species': species}
    occur_per_species = requests.get(f'{base_url}{search_url}', params=params)
    occur_per_species = json.loads(occur_per_species.content)


    return occur_per_species

    
if __name__ == "__main__":   
    
    one_species_list = herb_location('2020', 'Ambrosia artemisiifolia')

    print(f"""
    Вид: {one_species_list['scientificName']}, 
    место обнаружения: {one_species_list['decimalLongitude']}, {one_species_list['decimalLatitude']}, 
    район обнаружения: {one_species_list['gadm']}, 
    год обнаружения: {one_species_list['year']}.""")