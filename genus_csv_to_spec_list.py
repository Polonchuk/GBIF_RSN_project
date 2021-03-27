import csv
import json

# Открываем файл, полученный в результате запроса о встречаемости всех видов определенного рода ("gbif_downl_api_genus.py").

with open('0220459-200613084148143.csv', encoding='utf-8') as r_file:
    species_occurrence = csv.DictReader(r_file, delimiter='\t')

# Создаем список для сбора уникальных названий видов

    species_list = []

# Из строк данных о встреченных видах выбираем названия видов...

    for row in species_occurrence:
#        species_name = row['species']
#        full_species_name = row['scientificName']
        taxon_Key = row['taxonKey']
#        new_species = {'species_name' : row['species'], 'full_species_name' : row['scientificName'], 'taxon_Key' : row['taxonKey']}

# ... и сохраняем каждое из названий один раз.
#        for dict_element in species_list:

        if taxon_Key not in species_list:
            species_list.append(taxon_Key)

# print(species_list)

# Сохраняем список встреченных видов указанного рода. 

with open("per_species_data.json", "w") as a_file:
    json.dump(species_list, a_file)