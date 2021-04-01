from db import db_session
from db_models import Herb_species, Info_source

plants_list = [
    {"scientific_name": "Acroptilon repens", "Full_name": "Горчак ползучий (Acroptilon repens DC)", "genus": "Acroptilon", "status": "present"},
    {"scientific_name": "Ambrosia artemisiifolia", "Full_name": "Амброзия полыннолистная (Ambrosia artemisiifolia L)", "genus": "Ambrosia", "status": "present"},
    {"scientific_name": "Ambrosia psilostachya", "Full_name": "Амброзия многолетняя (Ambrosia psilostachya DC.)", "genus": "Ambrosia", "status": "present"},
    {"scientific_name": "Ambrosia trifida", "Full_name": "Амброзия трехраздельная (Ambrosia trifida L)", "genus": "Ambrosia", "status": "present"},
    {"scientific_name": "Cenchrus longispinus", "Full_name": "Ценхрус длинноколючковый (Cenchrus longispinus (Hackel) Fernald)", "genus": "Cenchrus", "status": "present"},
    {"scientific_name": "Solanum rostratum", "Full_name": "Паслен колючий (Solanum rostratum Dun.)", "genus": "Solanum", "status": "present"},
    {"scientific_name": "Solanum triflorum", "Full_name": "Паслен трехцветковый (Solanum triflorum Nutt.)", "genus": "Solanum", "status": "present"},
    {"scientific_name": "Cuscuta lupuliformis", "Full_name": "_Повилика хмелевидная_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta campestris", "Full_name": "Повилика полевая (Cuscuta campestris Juncker)", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta europaea", "Full_name": "Повилика европейская (Cuscuta europaea)", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta epithymum", "Full_name": "_Повилика тимьяновая_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta japonica", "Full_name": "_Повилика японская_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta approximata", "Full_name": "_Повилика сближенная_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta scandens", "Full_name": "_Повилика лазящая_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta monogyna", "Full_name": "_Повилика одностолбиковая_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Bidens pilosa", "Full_name": "Череда волосистая (Bidens pilosa L.)", "genus": "Bidens", "status": "absent"},
    {"scientific_name": "Euphorbia dentata", "Full_name": "Молочай зубчатый (Euphorbia dentata Michx.)", "genus": "Euphorbia", "status": "absent"},
    {"scientific_name": "Helianthus californicus", "Full_name": "Подсолнечник калифорнийский (Helianthus californicus DC.)", "genus": "Helianthus", "status": "absent"},
    {"scientific_name": "Helianthus ciliaris", "Full_name": "Подсолнечник реснитчатый (Helianthus ciliaris DC.)", "genus": "Helianthus", "status": "absent"},
    {"scientific_name": "Ipomoea hederacea", "Full_name": "Ипомея плющевидная (Ipomoea hederacea L.)", "genus": "Ipomoea", "status": "absent"},
    {"scientific_name": "Ipomoea lacunosa", "Full_name": "Ипомея ямчатая (Ipomoea lacunosa L.)", "genus": "Ipomoea", "status": "absent"},
    {"scientific_name": "Iva axillaris", "Full_name": "Бузинник пазушный (Iva axillaris Pursh.)", "genus": "Iva", "status": "absent"},
    {"scientific_name": "Solanum carolinense", "Full_name": "Паслен каролинский (Solanum carolinense L.)", "genus": "Solanum", "status": "absent"},
    {"scientific_name": "Solanum elaeagnifolium", "Full_name": "Паслен линейнолистный (Solanum elaeagnifolium Cav.)", "genus": "Solanum", "status": "absent"},
    {"scientific_name": "Cuscuta spp.", "Full_name": "Повилики (Cuscuta spp.)", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta lehmaniana", "Full_name": "Повилика Лемана (Cuscuta lehmaniana Bunge).", "genus": "Cuscuta", "status": "present"}
]

db_session.bulk_insert_mappings(Herb_species, plants_list, return_defaults=True)
db_session.commit()

sources_list = [
    {"alias": "gbif", "full_name": "Глобальная информационная система о биоразнообразии (Global Biodiversity Information Facility)"},
    {"alias": "rsn", "full_name": "Федеральная служба по ветеринарному и фитосанитарному надзору (Россельхознадзор)"}
]

db_session.bulk_insert_mappings(Info_source, sources_list, return_defaults=True)
db_session.commit()