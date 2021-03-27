import csv, json, string

list_plants = [ "Acroptilon repens",
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
    "Cuscuta spp.",
    "Cuscuta lehmaniana"
]

string_dict = []
ir_dict = []

with open('data-zones.csv', encoding='utf-8') as r_file:
    zones_list = csv.DictReader(r_file, delimiter=',')
    ok_counter = 0
    fail_counter = 0
#    test_counter_ok = 0
#    test_counter_fail = 0
    right_species_counter = 0
    wrong_species_counter = 0

    for row in zones_list:
        herb_defined = False
        full_name = row["Наименование карантинного вредного организма"]
        for plant in list_plants:
            if plant in full_name:
                      
                order = row["№ и дата приказа об установлении карантинной фитосанитарной зоны"]
                region = row["Регион"]
                fed_district = row["Федеральный округ"]
                right_species_counter += 1
                herb_defined = True
   
  
# Добавляем указание рода для нужного нам рода:
                sc_name_split = plant.split()
                if sc_name_split[0] == 'Cuscuta':
                    genus = 'Cuscuta'
                else:
                    genus = 'genus'

                order_split = order.split()
                have_a_date = False
                for order_element in order_split:
# Проверяем каждый отдельный (отделенный пробелами) элемент строки "приказ" на соответствие формату даты.
                    if len(order_element) >= 4:
                        to_be_figure_1 = order_element[0]
                        to_be_figure_2 = order_element[3]

                    if len(order_element) >= 8 and to_be_figure_1.isdigit() and order_element[2]=='.' and to_be_figure_2.isdigit() and order_element[5] =='.':

# Удаляем пустые елементы списка, возникающие, когда у нас есть две точки подряд.                            
                        date_split = order_element.split('.')
                        for date_element in date_split:
                            if date_element == '':
                                date_split.remove(date_element)


# Проверяем третий численный элемент на соответствие формату года:                            
                        to_be_year = date_split[2]

# Если третий элемент сразу соответствует формату года:
                        if to_be_year.isdigit() and len(to_be_year) == 4:

# Проверяем, не прицепились ли вслед за годом лишние элементы:                            
                            if len(date_split) == 3:
                                date = ".".join(date_split)
                                year = to_be_year
                                have_a_date = True


                            else:
                                date_split = date_split[:3]
                                date = ".".join(date_split)
                                year = to_be_year
                                have_a_date = True
                            ok_counter += 1
# Если третий элемент формату года не соответствует, то набираем год из имеющихся цифр:
                        else:                            
                            year = ''
                            figure_count = 0
                            for figure in to_be_year:
                                if figure.isdigit():
                                    year = year + figure
                                    figure_count += 1
# Если цифр в годе одна или три, то год распознать нельзя:
                            if figure_count < 2 or figure_count == 3:
                                have_a_date = False
                                fail_counter += 1

# Если цифр в годе две, исправляем год:
                            elif figure_count == 2:
                                year = '20' + year
                                date_split = date_split[:2]
                                date_split.append(year)
                                date = ".".join(date_split)
                                have_a_date = True
                                ok_counter += 1

# Если цифр в годе осталось четыре (после удаления нечисленных символов), то хорошо:                                
                            elif figure_count == 4:                               
                                date_split = date_split[:2]
                                date_split.append(year)
                                date = ".".join(date_split)
                                have_a_date = True
                                ok_counter += 1        

# Если с дальнейшим распознаванием дата-подобного объекта не клеится:
                            else:
                                have_a_date = False
                                fail_counter += 1

# Если дата была распознана:
                        if have_a_date == True:   
                            
                            string_dict.append({
                                'scientific_name': plant,
                                'full_name': full_name,
                                'genus': genus,
                                'longitude': "Добавить",
                                'latitude': "Добавить",
                                'region': region,
                                'fed_district': fed_district,
                                'year': year,
                                'date': date,
                                'order': order,
                                'link': 'link',
                                'source': 'rsn'
                                })   
# Если дата не была найдена или распознана:            
                if have_a_date == False:
                    fail_counter += 1
                    print(f'В приказе {order} дата не определена. Список разделен на: {order_split}')

                    string_dict.append({
                        'scientific_name': plant, 
                        'full_name': full_name,
                        'genus': genus,
                        'longitude': 'Добавить', 
                        'latitude': 'Добавить', 
                        'region': region, 
                        'fed_district': fed_district, 
                        'year': 'Дата не определена для этого приказа!!!', 
                        'date': 'Дата не определена для этого приказа!!!', 
                        'order': order, 
                        'link': 'link', 
                        'source': 'rsn'
                        })
                
                    

        if herb_defined == False:
            wrong_species_counter += 1
            if full_name not in ir_dict:
                ir_dict.append(full_name)


    print(f'Дата распознана {ok_counter} раз.')
    print(f'Дата не распознана {fail_counter} раз.')
    print(f'Количество приказов по интересующим видам: {right_species_counter}')
    print(f'Количество приказов по прочим видам: {wrong_species_counter}')


with open("rsn_all_species_data.json", "w", encoding='utf-8') as a_file:
        json.dump(string_dict, a_file, ensure_ascii=False)

with open("irrelevant_1.json", "w", encoding='utf-8') as b_file:
        json.dump(ir_dict, b_file, ensure_ascii=False)


