from db import db_session
from models import Herb_species, Info_source

plants_list = [
    {"scientific_name": "Acroptilon repens", "full_name": "Горчак ползучий (Acroptilon repens DC)", "genus": "Acroptilon", "status": "present"},
    {"scientific_name": "Ambrosia artemisiifolia", "full_name": "Амброзия полыннолистная (Ambrosia artemisiifolia L)", "genus": "Ambrosia", "status": "present"},
    {"scientific_name": "Ambrosia psilostachya", "full_name": "Амброзия многолетняя (Ambrosia psilostachya DC.)", "genus": "Ambrosia", "status": "present"},
    {"scientific_name": "Ambrosia trifida", "full_name": "Амброзия трехраздельная (Ambrosia trifida L)", "genus": "Ambrosia", "status": "present"},
    {"scientific_name": "Cenchrus longispinus", "full_name": "Ценхрус длинноколючковый (Cenchrus longispinus (Hackel) Fernald)", "genus": "Cenchrus", "status": "present"},
    {"scientific_name": "Solanum rostratum", "full_name": "Паслен колючий (Solanum rostratum Dun.)", "genus": "Solanum", "status": "present"},
    {"scientific_name": "Solanum triflorum", "full_name": "Паслен трехцветковый (Solanum triflorum Nutt.)", "genus": "Solanum", "status": "present"},
    {"scientific_name": "Cuscuta lupuliformis", "full_name": "_Повилика хмелевидная_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta campestris", "full_name": "Повилика полевая (Cuscuta campestris Juncker)", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta europaea", "full_name": "Повилика европейская (Cuscuta europaea)", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta epithymum", "full_name": "_Повилика тимьяновая_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta japonica", "full_name": "_Повилика японская_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta approximata", "full_name": "_Повилика сближенная_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta scandens", "full_name": "_Повилика лазящая_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta monogyna", "full_name": "_Повилика одностолбиковая_", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Bidens pilosa", "full_name": "Череда волосистая (Bidens pilosa L.)", "genus": "Bidens", "status": "absent"},
    {"scientific_name": "Euphorbia dentata", "full_name": "Молочай зубчатый (Euphorbia dentata Michx.)", "genus": "Euphorbia", "status": "absent"},
    {"scientific_name": "Helianthus californicus", "full_name": "Подсолнечник калифорнийский (Helianthus californicus DC.)", "genus": "Helianthus", "status": "absent"},
    {"scientific_name": "Helianthus ciliaris", "full_name": "Подсолнечник реснитчатый (Helianthus ciliaris DC.)", "genus": "Helianthus", "status": "absent"},
    {"scientific_name": "Ipomoea hederacea", "full_name": "Ипомея плющевидная (Ipomoea hederacea L.)", "genus": "Ipomoea", "status": "absent"},
    {"scientific_name": "Ipomoea lacunosa", "full_name": "Ипомея ямчатая (Ipomoea lacunosa L.)", "genus": "Ipomoea", "status": "absent"},
    {"scientific_name": "Iva axillaris", "full_name": "Бузинник пазушный (Iva axillaris Pursh.)", "genus": "Iva", "status": "absent"},
    {"scientific_name": "Solanum carolinense", "full_name": "Паслен каролинский (Solanum carolinense L.)", "genus": "Solanum", "status": "absent"},
    {"scientific_name": "Solanum elaeagnifolium", "full_name": "Паслен линейнолистный (Solanum elaeagnifolium Cav.)", "genus": "Solanum", "status": "absent"},
    {"scientific_name": "Cuscuta spp.", "full_name": "Повилики (Cuscuta spp.)", "genus": "Cuscuta", "status": "present"},
    {"scientific_name": "Cuscuta lehmaniana", "full_name": "Повилика Лемана (Cuscuta lehmaniana Bunge).", "genus": "Cuscuta", "status": "present"}
]

db_session.bulk_insert_mapping(Herb_species, plants_list, return_dafaults=True)
db_session.commit()

sources_list = [
    {"alias": "gbif", "full_name": "Глобальная информационная система о биоразнообразии (Global Biodiversity Information Facility)"},
    {"alias": "rsn", "full_name": "Федеральная служба по ветеринарному и фитосанитарному надзору (Россельхознадзор)"}
]

db_session.bulk_insert_mapping(Info_source, sources_list, return_dafaults=True)
db_session.commit()