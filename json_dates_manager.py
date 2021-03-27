import json, string

with open('rsn_all_species_corrected_dates.json', encoding='utf-8') as r_file:
    all_dates = json.load(r_file)

    refined_dates_records = []
    fine_dates = 0
    old_dates = 0

    for record in all_dates:
        record_year = int(record['year'])
        if record_year > 2015:
            refined_dates_records.append(record)
            fine_dates += 1
        else:
            old_dates += 1

print(f'Общая длина списка была: {len(all_dates)}.')
print(f'Общая длина списка стала: {len(refined_dates_records)}.')
print(f'Учтено добавленных записей: {fine_dates}.')
print(f'Учтено изъятых записей: {old_dates}.')

with open('rsn_all_species_required_dates.json', 'w', encoding='utf-8') as w_file:
        json.dump(refined_dates_records, w_file, ensure_ascii=False)