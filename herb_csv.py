import csv, json, string

list_plants = [ "Acroptilon repens",
            "Ambrosia artemisiifolia",
            "Ambrosia psilostachya",
            "Ambrosia trifida",
            "Cenchrus longispinus",
            "Solanum rostratum",
            "Solanum triflorum"
            "Solanum carolinense",
            "Cuscuta",
            "Bidens pilosa",
            "Euphorbia dentata",
            "Helianthus californicus",
            "Helianthus ciliaris",
            "Ipomoea lacunosa",
            "Helianthus ciliaris",
            "Iva axillaris",
]
string_dict = []
#s_dict = []

with open('data-zones.csv', encoding='utf-8') as r_file:
    zones_list = csv.DictReader(r_file, delimiter=',')
    for row in zones_list:
        for plant in list_plants:
            if plant in row["Наименование карантинного вредного организма"]:
                ru_name = row["Наименование карантинного вредного организма"]
                name = row["Наименование карантинного вредного организма"]              
                data_order = row["№ и дата приказа об установлении карантинной фитосанитарной зоны"]
                data = row["№ и дата приказа об установлении карантинной фитосанитарной зоны"]
                date = data.split(' ')
 
                string_dict.append({'scientific_name': plant, 'ru_name': ru_name, 'longitude': "Добавить", 'latitude': "Добавить", 'region': "region1", 'sub-region': "region2", 'year': date[-1], 'order': data_order, 'link': 'link', 'source': 'rsn'})
            #else:
                #if row["Наименование карантинного вредного организма"] not in s_dict:
                    #s_dict.append(row["Наименование карантинного вредного организма"])

with open("rsn_all_species_data.json", "w", encoding='utf-8') as a_file:
        json.dump(string_dict, a_file, ensure_ascii=False)
#with open("check.json", "w", encoding='utf-8') as a_file:
        #json.dump(s_dict, a_file, ensure_ascii=False)

