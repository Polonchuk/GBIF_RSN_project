import json, csv

with open('rsn_all_species_with_coord_no_crimea_final.json', encoding='utf-8') as r_file:
    all_rsn_records = json.load(r_file)

    regions_rsn_dict = {}

    for record in all_rsn_records:
        region = record['region']
        if region not in regions_rsn_dict.keys():
            regions_rsn_dict[region] = 1
        else:
            regions_rsn_dict[region] += 1

    regions_data = []

    for rsn_region in regions_rsn_dict.keys():
        if regions_rsn_dict[rsn_region] > 20:
            region_record = {
                'region_id': 'Добавить', 
                'region_name': rsn_region, 
                'occurrences': regions_rsn_dict[rsn_region]
                }
        
            regions_data.append(region_record)


with open('rsn_occurrences_per_region.csv', 'w', newline='', encoding='utf-8') as a_file:
    columns = ['region_id', 'region_name', 'occurrences']
    writer = csv.DictWriter(a_file, fieldnames=columns)
    writer.writeheader()     
    writer.writerows(regions_data)