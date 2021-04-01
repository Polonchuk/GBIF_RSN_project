import json, string

with open('gbif_all_species_data_regions_corrected.json', encoding='utf-8') as r_file:
    all_records = json.load(r_file)

    decimal_coordinates_records = []
    count_final = 0
    
    for record in all_records:
        
        longitude = float(record['longitude']) 
        latitude = float(record['latitude'])


        if longitude == None or longitude == 0 or latitude == None or latitude == 0:
            lat = record['latitude']
            lon = record['longitude']
            print(f'Координаты не распознаны! latitude: {lat}, longitude {lon}.')
        
        else:

            decimal_coordinates_records.append({
            'scientific_name': record['scientific_name'], 
            'longitude': longitude, 
            'latitude': latitude, 
            'region': record['region'], 
            'year': int(record['year']), 
            'alias': record['source']
            })
            count_final += 1



with open('gbif_all_species_data_coordinates_decimal.json', 'w', encoding='utf-8') as w_file:
        json.dump(decimal_coordinates_records, w_file, ensure_ascii=False)

print(f'Всего строк обработано: {count_final}')