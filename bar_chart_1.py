import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

with open('rsn_occurrences_per_region_filled_with_exclusions.csv', encoding='utf-8') as r_file:
    regions_data = csv.DictReader(r_file, delimiter=',')


    region_names = []
    region_occ = []
    region_crops = []

    for record in regions_data:
        occ = int(record['occurrences'])
        crops = float(record['crops_area_in_region'])/10 # величину "количество посевных площадей" уменьшаем в 10 раз, чтобы масштабировать со второй величиной
        reg_name = record['region_name'].split()
        reg_name_adjust = '\n'.join(reg_name)
        region_names.append(reg_name_adjust)
        region_occ.append(occ)
        region_crops.append(crops)


x = np.arange(len(region_names))  # распределяем названия регионов
width = 0.35  # ширина столбцов

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, region_occ, width, label='Очаги всех карантинных растений в области')
rects2 = ax.bar(x + width/2, region_crops, width, label='Общее количество посевных площадей в области, 10 тыс. га')

# Заголовки осей и легенда
ax.set_ylabel('Количество выявленных очагов / посевные площади (10 000 га)')
ax.set_title('Выбранные для сравнения области')
ax.set_xticks(x)
ax.set_xticklabels(region_names)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()