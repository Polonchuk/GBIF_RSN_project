import csv
import json

# Открываем файл, полученный в результате запроса о встречаемости всех видов определенного рода ("gbif_downl_api_genus...").

with open('0211817-200613084148143.csv', encoding='utf-8') as r_file:
    species_occurrence = csv.DictReader(r_file, delimiter='\t')

# Создаем список для сбора уникальных названий видов

    species_list = []

# Из строк данных о встреченных видах выбираем названия видов...

    for row in species_occurrence:
        species_name = row["scientificName"]

# ... и сохраняем каждое из названий один раз.

        if species_name not in species_list:
            species_list.append(species_name)

print(species_list)

# Сохраняем список встреченных видов указанного рода. После добавления полученного списка видов в файл 'data_objects_herb_present'
# при вызове 'gbif_occur_api_spec_list' мы можем вместо названия рода оперировать только названиями видов.

with open("per_species_data.json", "w") as a_file:
    json.dump(species_list, a_file)