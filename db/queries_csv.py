from db import db_session
from db_models import Herb_species, Herb_occurrence, Info_source
import csv


herbs_records = db_session.query(Herb_occurrence, Herb_species).join(Herb_species, Herb_occurrence.scientific_name_id == Herb_species.id).all()

db_data = []

for record, species in herbs_records:
    if record.source_id == 9:
        source = 'gbif'
    else:
        source = 'rsn'
    db_record = {
        'occurrence_id': record.id, 
        'latitude': record.latitude, 
        'longitude': record.longitude, 
        'region': record.region, 
        'year': record.year, 
        'scientific_name': species.scientific_name, 
        'full_name': species.Full_name, 
        'genus': species.genus, 
        'status': species.status, 
        'source_alias': source
        }
    
    db_data.append(db_record)


with open('db_data.csv', 'w', newline='', encoding='utf-8') as a_file:
    columns = ['occurrence_id', 'latitude', 'longitude', 'region', 'year', 'scientific_name', 'full_name', 'genus', 'status', 'source_alias']
    writer = csv.DictWriter(a_file, fieldnames=columns)
    writer.writeheader()     
    writer.writerows(db_data)
   

