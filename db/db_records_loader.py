import json
from db import db_session
from db_models import Herb_species, Info_source, Herb_occurrence

species_id_dict = [
{"id": 105, "scientific_name": "Acroptilon repens"},
{"id": 106, "scientific_name": "Ambrosia artemisiifolia"},
{"id": 107, "scientific_name": "Ambrosia psilostachya"},
{"id": 108, "scientific_name": "Ambrosia trifida"},
{"id": 109, "scientific_name": "Cenchrus longispinus"},
{"id": 110, "scientific_name": "Solanum rostratum"},
{"id": 111, "scientific_name": "Solanum triflorum"},
{"id": 112, "scientific_name": "Cuscuta lupuliformis"},
{"id": 113, "scientific_name": "Cuscuta campestris"},
{"id": 114, "scientific_name": "Cuscuta europaea"},
{"id": 115, "scientific_name": "Cuscuta epithymum"},
{"id": 116, "scientific_name": "Cuscuta japonica"},
{"id": 117, "scientific_name": "Cuscuta approximata"},
{"id": 118, "scientific_name": "Cuscuta scandens"},
{"id": 119, "scientific_name": "Cuscuta monogyna"},
{"id": 120, "scientific_name": "Bidens pilosa"},
{"id": 121, "scientific_name": "Euphorbia dentata"},
{"id": 122, "scientific_name": "Helianthus californicus"},
{"id": 123, "scientific_name": "Helianthus ciliaris"},
{"id": 124, "scientific_name": "Ipomoea hederacea"},
{"id": 125, "scientific_name": "Ipomoea lacunosa"},
{"id": 126, "scientific_name": "Iva axillaris"},
{"id": 127, "scientific_name": "Solanum carolinense"},
{"id": 128, "scientific_name": "Solanum elaeagnifolium"},
{"id": 129, "scientific_name": "Cuscuta spp."},
{"id": 130, "scientific_name": "Cuscuta lehmaniana"}
]

sources_id_dict = [
{"id": 9, "alias": "gbif"},
{"id": 10, "alias": "rsn"}
]

with open('gbif_all_species_data_coordinates_decimal.json', encoding='utf-8') as rec_file:
    all_records = json.load(rec_file)
    formated_records = []
    for record in all_records:
        species_found = False
        source_found = False
        for species_id in species_id_dict:
            if record["scientific_name"] == species_id["scientific_name"]:
                scientific_name_id = species_id["id"]
                species_found = True
        for source in sources_id_dict:
            if record["alias"] == source["alias"]:
                source_id = source["id"]
                source_found = True

        if species_found == False:
            sp_n = record["scientific_name"]
            print(f'Вид не найден: {sp_n}')
        else:
            if source_found == False:
                al = record["alias"]
                print(f'Источник не найден: {al}')
            else:
                formed_record = {"latitude": record["latitude"], "longitude": record["longitude"], "region": record["region"], "year": record["year"], "scientific_name_id": scientific_name_id, "source_id": source_id}
                formated_records.append(formed_record)


db_session.bulk_insert_mappings(Herb_occurrence, formated_records, return_defaults=True)
db_session.commit()


