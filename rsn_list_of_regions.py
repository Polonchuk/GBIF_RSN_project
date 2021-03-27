import json, string

with open('rsn_all_species_with_coord.json', encoding='utf-8') as r_file:
    all_regions = json.load(r_file)

    rsn_regions_list = []

    for record in all_regions:
        if  record['region'] not in rsn_regions_list:
            rsn_regions_list.append(record['region'])

print(f'Количество регионов: {len(rsn_regions_list)}.')

with open('rsn_regions_list.json', 'w', encoding='utf-8') as y_file:
        json.dump(rsn_regions_list, y_file, ensure_ascii=False)