import csv
import json

# Референсные названия видов карантинных растений для унификации со списком РосСельхоза:

species_reference_list = [
"Acroptilon repens",
"Ambrosia artemisiifolia",
"Ambrosia psilostachya",
"Ambrosia trifida",
"Cenchrus longispinus",
"Solanum rostratum",
"Solanum triflorum",
"Cuscuta lupuliformis",
"Cuscuta campestris",
"Cuscuta europaea",
"Cuscuta epithymum",
"Cuscuta japonica",
"Cuscuta approximata",
"Cuscuta scandens",
"Cuscuta monogyna",
"Bidens pilosa",
"Euphorbia dentata",
"Helianthus californicus",
"Helianthus ciliaris",
"Ipomoea hederacea",
"Ipomoea lacunosa",
"Iva axillaris",
"Solanum carolinense",
"Solanum elaeagnifolium",
]

# Референсные названия регионов для унификации со списком РосСельхоза:

regions_reference = {
"Adygey": "Республика Адыгея",
"Amur": "Амурская область",
"Amur Oblast": "Амурская область",
"Arkhangel'sk": "Астраханская область",
"Bashkortostan": "Республика Башкортостан",
"Belgorod": "Белгородская область",
"Bryansk": "Брянская область",
"Chelyabinsk": "Челябинская область",
"Chuvash": "Чувашская Республика",
"City of St. Petersburg": "Ленинградская область",
"Dagestan": "Республика Дагестан",
"Gorno-Altay": "Республика Алтай",
"Irkutsk": "Иркутская область",
"Kabardin-Balkar": "КБР",
"Kalmyk": "Республика Калмыкия",
"Kaluga": "Калужская область",
"Karachay-Cherkess": "Карачаево-Черкесская Республика",
"Kemerovo": "Кемеровская область",
"Khakass": "Республика Хакасия",
"Kostroma": "Костромская область",
"Krasnodar": "Краснодарский край",
"Krasnodar Krai": "Краснодарский край",
"Krasnoyarsk": "Красноярский край",
"Kursk": "Курская область",
"Leningrad": "Ленинградская область",
"Lipetsk": "Липецкая область",
"Mordovia": "Республика Мордовия",
"Moscow": "Московская область",
"Moscow City": "Московская область",
"Moscow Oblast": "Московская область",
"Moscow Region": "Московская область",
"Moskva": "Московская область",
"Nizhegorod": "Нижегородская область",
"Nizhny Novgorod Oblast": "Нижегородская область",
"North Ossetia": "Республика Северная Осетия-Алания",
"Novosibirsk": "Новосибирская область",
"Omsk": "Омская область",
"Orenburg": "Оренбургская область",
"Orenburg Oblast": "Оренбургская область",
"Penza": "Пензенская область",
"Perm": "Пермский край",
"Primor'ye": "Приморский край",
"Pskov": "Псковская область",
"Rostov Oblast": "Ростовская область",
"Ryazan Oblast": "Рязанская область",
"Sakhalin": "Сахалинская область",
"Samara": "Самарская область",
"Samara Oblast": "Самарская область",
"Samarskaia oblast": "Самарская область",
"Saratov": "Саратовская область",
"Saratov Oblast": "Саратовская область",
"Stavropol": "Ставропольский край",
"Stavropol'": "Ставропольский край",
"Stavropol Krai": "Ставропольский край",
"Sverdlovsk": "Свердловская область",
"Tambov": "Тамбовская область",
"Tatarstan": "Республика Татарстан",
"Tomsk": "Томская область",
"Tula": "Тульская область",
"Tver": "Тверская область",
"Tver'": "Тверская область",
"Tver Oblast": "Тверская область",
"Tyumen'": "Тюменская область",
"Udmurt": "Удмуртская Республика",
"Ulianovskaia oblast": "Ульяновская область",
"Ul'yanovsk": "Ульяновская область",
"Vladimir": "Владимирская область",
"Volgograd": "Волгоградская область",
"Volgograd Oblast": "Волгоградская область",
"Voronezh": "Воронежская область",
"Voronezh Oblast": "Воронежская область",
"Yaroslavl": "Ярославская область",
"Yaroslavl'": "Ярославская область",
"Yaroslavl Oblast": "Ярославская область",
"Белгородская область": "Белгородская область"
}

# Открываем файл, полученный в результате запроса о встречаемости всех нужных нам видов в 2016-2020 годах ("gbif_downl_api_species.py").

no_region_counter = 0

with open('0222448-200613084148143.csv', encoding='utf-8') as r_file:
    species_raw_data = csv.DictReader(r_file, delimiter='\t')

#    with open('data_objects_herbs_present.csv', encoding='utf-8') as r_file:
#        species_reference_list = csv.DictReader(r_file, delimiter=',')

    all_species_fine_data = []

    for species_occurrence in species_raw_data:
        species_in_record = species_occurrence['species']
        species_in_record_split = species_in_record.split()
        scientific_name_in_record = species_occurrence['scientificName']
        scientific_name_in_record_split = scientific_name_in_record.split()
        species_record_id = species_occurrence['gbifID']
        reference_found = False

# Для каждой записи в списке встреченных видов находим соответствующее референсное название вида для унификации со списком РосСельхоза:

        for reference_name in species_reference_list:
#            species_name_standard = reference_name["Latin"]
            species_name_standard_split = reference_name.split()
            if  species_in_record_split[0] == species_name_standard_split[0] and species_in_record_split[1] == species_name_standard_split[1]:
                scientific_name = reference_name
                reference_found = True
            elif scientific_name_in_record_split[0] == species_name_standard_split[0] and scientific_name_in_record_split[1] == species_name_standard_split[1]:
                scientific_name = reference_name
                reference_found = True

        if reference_found == False:
            scientific_name = 'Undefined!'
            print(f'Для вида {species_in_record} в записи gbifID {species_record_id} название не соотнесено с эталонным списком видов.')

# Получаем остальные нужные нам параметры в дополнение к названию вида:

        longitude = species_occurrence.get('decimalLongitude')
        if longitude == None or longitude == '':
            print(f'Для вида {species_in_record} в записи gbifID {species_record_id} не определена ДОЛГОТА.')
            continue
        latitude = species_occurrence.get('decimalLatitude')
        if latitude == None or latitude == '':
            print(f'Для вида {species_in_record} в записи gbifID {species_record_id} не определена ШИРОТА.')
            continue
        
        region_verbatim = species_occurrence.get('stateProvince')
        
        if region_verbatim in regions_reference.keys():
            region = regions_reference[region_verbatim]
        else:
            region_verbatim_split = region_verbatim.split()
            sep = '_'
            region_verbatim_join = sep.join(region_verbatim_split)
            name_match = False
            for name_key in regions_reference.keys():
                name_key_split = name_key.split()
                name_key_join = sep.join(name_key_split)
                if region_verbatim_join == name_key_join:
                    region = regions_reference[name_key]
#                    print(f'Определено при обработке: {region_verbatim} это {name_key}')
                    name_match = True

            if name_match == False:
                region = "not defined"
                locality_verbatim = species_occurrence.get('locality')
#                print(f'Не определено! stateProvince: {region_verbatim}, locality: {locality_verbatim}')
                no_region_counter += 1
                

        year = species_occurrence.get('year')
        if year == None or year == '':
            print(f'Для вида {species_in_record} в записи gbifID {species_record_id} не определен год находки.')

# Добавляем указание рода для нужного нам рода:
        sc_name_split = scientific_name.split()
        genus = sc_name_split[0]

        if genus == "" or genus == None:
            print(f'Род не определен!')


# Записываем нужные данные по всем встреченным видам в общий список (словарей):
        all_species_fine_data.append({
            'scientific_name': scientific_name,
            'genus': genus, 
            'longitude': longitude, 
            'latitude': latitude, 
            'region': region, 
            'year': year, 
            'source': 'gbif'
            })

print(len(all_species_fine_data))
print(f'Регион не определен для {no_region_counter} находок.')

# Сохраняем данные в файл

with open("gbif_all_species_data_regions.json", "w", encoding='utf-8') as a_file:
    json.dump(all_species_fine_data, a_file, ensure_ascii=False)