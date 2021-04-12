import json, csv

with open('geo.json', encoding='utf-8') as g_file:
    geo_data = json.load(g_file)

regions_list = geo_data['features']
regions_data = []

for record in regions_list:

    region_record = {
        'region_id': record['properties']['ID_1'], 
        'region_name': record['properties']['NAME_1'], 
        'farmland_percentage': 'Добавить'
        }
    
    regions_data.append(region_record)


with open('regions_farmland_data.csv', 'w', newline='', encoding='utf-8') as a_file:
    columns = ['region_id', 'region_name', 'farmland_percentage']
    writer = csv.DictWriter(a_file, fieldnames=columns)
    writer.writeheader()     
    writer.writerows(regions_data)