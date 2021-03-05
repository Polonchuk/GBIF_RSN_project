import requests
import json

def herb_location(year, scientific_name):
    base_url = 'https://api.gbif.org/v1/'
    search_url = 'occurrence/search'
    params = {'country': 'RU', 'year': year, 'scientific_name': scientific_name}
    occur_per_species = requests.get(f'{base_url}{search_url}', params=params)
    occur_per_species = json.loads(occur_per_species.content)


    return occur_per_species

    
if __name__ == "__main__":   
    
    one_species_list = herb_location('2020', 'Ambrosia artemisiifolia L.')

#    print(one_species_list.keys())

    species_raw_data = (one_species_list['results'])
    species_fine_data = []
    
    for data_extract in species_raw_data:
        scientific_name = data_extract.get('scientificName')
        longitude = data_extract.get('decimalLongitude')
        latitude = data_extract.get('decimalLatitude')
        region = data_extract.get('gadm')
        year = data_extract.get('year')

        species_fine_data.append({'scientific_name': scientific_name, 'longitude': longitude, 'latitude': latitude, 'region': region, 'year': year})


#    print(len(species_raw_data))

with open("per_species_data.json", "w") as a_file:
    json.dump(species_fine_data, a_file)

        

