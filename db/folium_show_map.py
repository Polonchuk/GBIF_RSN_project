import folium
import pandas as pd
from db import db_session
from db_models import Herb_species, Herb_occurrence, Info_source

species_colourcode = {
"Acroptilon repens": 'orange',
"Ambrosia artemisiifolia": 'green',
"Ambrosia psilostachya": 'darkgreen',
"Ambrosia trifida": 'lightgreen',
"Cenchrus longispinus": 'darkred',
"Solanum rostratum": 'purple',
# darkpurple invisible!
"Solanum triflorum": 'purple',
"Cuscuta approximata": 'blue',
"Cuscuta campestris": 'darkblue',
"Cuscuta europaea": 'cadetblue',
"Cuscuta scandens": 'lightblue',
"Cuscuta spp.": 'grey',
# lightred invisible!
"Cuscuta epithymum": 'black',
"Cuscuta lupuliformis": 'pink',
"Cuscuta japonica": 'lightgray',
"Cuscuta monogyna": 'grey',
"Cuscuta lehmaniana": 'grey',
"Bidens pilosa": 'red',
"Euphorbia dentata": 'red',
"Helianthus californicus": 'red',
"Helianthus ciliaris": 'red',
"Ipomoea hederacea": 'red',
"Ipomoea lacunosa": 'red',
"Iva axillaris": 'red',
"Solanum carolinense": 'red',
"Solanum elaeagnifolium": 'red',
}


herbs_all_records = db_session.query(Herb_occurrence, Herb_species).join(Herb_species, Herb_occurrence.scientific_name_id == Herb_species.id).all()

my_map = folium.Map(location=[63, 87], zoom_start = 3)



def agro_choropleth(geo_file, csv_file):
    folium.GeoJson(data="C:\projects\GBIF_RSN_project\geo_data\geo.json").add_to(my_map)
    regions_farmland_data = pd.read_csv(csv_file)
    folium.Choropleth(
        geo_data=geo_file,
        name="choropleth",
        data=regions_farmland_data,
        columns=["region_id", "crops_area_in_region"],
        key_on="feature.properties.ID_1",
        fill_color="YlOrBr",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Посевные площади, тыс. га",
    ).add_to(my_map)

    folium.LayerControl().add_to(my_map)

    return my_map


def markers_placement(db_data):
    
    dots_number = 0
    for record, species in db_data:
        lat = record.latitude
        lon = record.longitude
        if species.scientific_name in species_colourcode.keys():
            dot_colour = species_colourcode[species.scientific_name]
        else:
            print(f'{species.scientific_name} не найден в словаре.')

        popup_text = species.scientific_name
        source = record.source_id
        if source == 9:
            folium.RegularPolygonMarker(location=[lat, lon], number_of_sides=3, popup=popup_text, radius = 3, color=dot_colour, fill=True, fill_color="black").add_to(my_map)
            

        elif source == 10:
            folium.CircleMarker(location=[lat, lon], popup=popup_text, radius = 3, color=dot_colour, fill=True, fill_color="black").add_to(my_map)
        else:
            print(f'Источник данных {record.source_id} не определен.')

        dots_number += 1
    print(dots_number)
    return my_map



if __name__ == '__main__':
    
    my_map = agro_choropleth(r'C:\projects\GBIF_RSN_project\geo_data\geo.json', r'C:\projects\GBIF_RSN_project\geo_data\full_regions_farmland_data.csv')
    my_map = markers_placement(herbs_all_records)
    my_map.save('index_choro2_all.html')
    