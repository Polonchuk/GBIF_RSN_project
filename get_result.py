import requests
import json


def herb_location(year, scientific_name, offset):
    base_url = 'https://api.gbif.org/v1/'
    search_url = 'occurrence/search'
    params = {
        'country': 'RU',
        'year': year,
        'scientific_name': scientific_name,
        'paging': True,
        'limit': 100,
        'offset': offset
    }
           
    occur_per_species = requests.get(f'{base_url}{search_url}', params=params)
    occur_per_species = json.loads(occur_per_species.content)
    
    return occur_per_species

    
if __name__ == "__main__":     


    one_species_list = herb_location('2020', 'Ambrosia artemisiifolia L.', offset=0)
    
    #    print(one_species_list.keys())

    offset = 0
    species_fine_data = []
    records_count = one_species_list['count']
    pages = (records_count // 100) + 1

# Проверка №1

    print(f'Базовый счетчик записей по запросу: {records_count} записей.')

    if records_count <= 100:
        species_raw_data = (one_species_list['results'])

        for data_extract in species_raw_data:
            scientific_name = data_extract.get('scientificName')
            longitude = data_extract.get('decimalLongitude')
            latitude = data_extract.get('decimalLatitude')
            region = data_extract.get('gadm')
            year = data_extract.get('year')

            species_fine_data.append({'scientific_name': scientific_name, 'longitude': longitude, 'latitude': latitude, 'region': region, 'year': year})

    else:
        for i in range(pages):
            
            one_species_list = herb_location('2020', 'Ambrosia artemisiifolia L.', offset=offset)
            species_raw_data = (one_species_list['results'])

            offset += 100

            for data_extract in species_raw_data:
                scientific_name = data_extract.get('scientificName')
                longitude = data_extract.get('decimalLongitude')
                latitude = data_extract.get('decimalLatitude')
                region = data_extract.get('gadm')
                year = data_extract.get('year')

                species_fine_data.append({'scientific_name': scientific_name, 'longitude': longitude, 'latitude': latitude, 'region': region, 'year': year})
    


# Проверка №2
    lenth_result = len(species_fine_data)
    print(f'Количество записей в сформированном файле: {lenth_result}.')

    with open("per_species_data.json", "w") as a_file:
        json.dump(species_fine_data, a_file)

        

