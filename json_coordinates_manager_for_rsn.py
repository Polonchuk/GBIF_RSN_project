import json, string

with open('rsn_all_species_with_coord_no_crimea_final.json', encoding='utf-8') as r_file:
    all_records = json.load(r_file)

    decimal_coordinates_records = []
    count_final = 0
    failed_coord = 0
    
    for record in all_records:
        try:
            longitude = float(record['longitude']) 
        except ValueError:
            order = record['order']
            print(f'Формат долготы некорректен в приказе {order}, строка {count_final + 1}')
            failed_coord += 1
        try:
            latitude = float(record['latitude'])
        except ValueError:
            order = record['order']
            print(f'Формат широты некорректен в приказе {order}, строка {count_final + 1}')
            failed_coord += 1


        if longitude == None or longitude == 0 or latitude == None or latitude == 0:
            print(f'Координаты не распознаны! {order}, строка {count_final + 1}')
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



with open('rsn_all_species_data_coordinates_decimal.json', 'w', encoding='utf-8') as w_file:
        json.dump(decimal_coordinates_records, w_file, ensure_ascii=False)

print(f'Всего строк обработано: {count_final}')
print(f'Ошибок в координатах: {failed_coord}')