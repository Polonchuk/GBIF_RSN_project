import requests
import json
import csv

# Функция запроса данных по обнаружениям вида с сайта GBIF в определенном году

def herb_location(species_name, offset):
    base_url = 'https://api.gbif.org/v1/'
    search_url = 'occurrence/search'
    params = {
        'country': 'RU',
        'year': '2020',
        'scientific_name': species_name,
        'paging': True,
        'limit': 100,
        'offset': offset
    }
           
    occur_per_species = requests.get(f'{base_url}{search_url}', params=params)
    occur_per_species = json.loads(occur_per_species.content)
    
    return occur_per_species

    
if __name__ == "__main__":     

# создаем список для хранения определенных (нужных) данных из запросов по всему списку видов

    all_species_fine_data = []

# Считываем из файла со списком интересующих видов названия видов

    with open('data_objects_herbs_present.csv', encoding='utf-8') as r_file:
        species_list = csv.DictReader(r_file, delimiter=',')
        for row in species_list:
            species_name = row["Latin"]

# первый запрос на получение с GBIF данных по названию вида из списка. Запрос на количество записей (обнаружений вида) в пределах "limit".

            one_species_list = herb_location(species_name, offset=0)
    
#    print(one_species_list.keys())

            offset = 0
            records_count = one_species_list['count']

# Вычисляем параметр для расчета "offset", - количества повторений количества записей по "limit" для получения полного списка записей по виду за указанный год.

            pages = (records_count // 100) + 1

# Проверка №1 Сколько записей учтено на сайте по указанному виду.

            print(f'Базовый счетчик записей по запросу {species_name}: {records_count} записей.')

# Если количество записей по виду в пределах  "limit":

            if records_count <= 100:
                species_raw_data = (one_species_list['results'])

# Собираем из всего массива данных только нужные нам для анализа

                for data_extract in species_raw_data:
                    scientific_name = data_extract.get('scientificName')
                    longitude = data_extract.get('decimalLongitude')
                    latitude = data_extract.get('decimalLatitude')
                    region = data_extract.get('gadm')
                    region1 = region.get('level1')
                    region2 = region.get('level2')
                    year = data_extract.get('year')

# Записываем нужные данные из запроса по одному виду в общий список (словарей) для всех запрашиваемых видов.

                    all_species_fine_data.append({'scientific_name': scientific_name, 'longitude': longitude, 'latitude': latitude, 'region': region1, 'sub-region': region2, 'year': year, 'source': 'gbif'})

# Если количество записей по одному виду больше  "limit":

            else:

# Задаем цикл для перебора всех "страниц" (offset) записей по одному виду:

                for i in range(pages):
            
                    one_species_list = herb_location(species_name, offset=offset)
                    species_raw_data = (one_species_list['results'])
                    offset += 100

# Собираем из всего массива данных только нужные нам для анализа

                    for data_extract in species_raw_data:
                        scientific_name = data_extract.get('scientificName')
                        longitude = data_extract.get('decimalLongitude')
                        latitude = data_extract.get('decimalLatitude')
                        region = data_extract.get('gadm')
                        region1 = region.get('level1')
                        region2 = region.get('level2')
                        year = data_extract.get('year')

# Записываем нужные данные из запроса по одному виду в общий список (словарей) для всех запрашиваемых видов.

                        all_species_fine_data.append({'scientific_name': scientific_name, 'longitude': longitude, 'latitude': latitude, 'region': region1, 'sub-region': region2, 'year': year, 'source': 'gbif'})
    

# Проверка №2 Сколько записей в итоге по всем видам содержит получившийся список словарей
    lenth_result = len(all_species_fine_data)
    print(f'Количество записей в сформированном файле для всех видов: {lenth_result}.')

# Сохраняем получившийся список словарей в файл

    with open("gbif_all_species_data.json", "w") as a_file:
        json.dump(all_species_fine_data, a_file)

        

