import json, string

with open('gbif_all_species_data.json', encoding='utf-8') as r_file:
    all_regions = json.load(r_file)

    regions_list = []

    for record in all_regions:
        if  record['region'] not in regions_list:
            regions_list.append(record['region'])

print(f'Количество регионов: {len(regions_list)}.')

with open('gbif_regions_list.json', 'w', encoding='utf-8') as y_file:
        json.dump(regions_list, y_file, ensure_ascii=False)