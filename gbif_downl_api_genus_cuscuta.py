import requests
# Файл аналогичен прокомментированному файлу "gbif_downl_api_genus_striga.py". Файл, сформированный в ответ на запрос, не скачивается по ссылке.
req_data = {
  "creator": "pavel_polonchuk",
  "notificationAddresses": [
    "Chelonpepk@gmail.com"
  ],
  "sendNotification": 'true',
  "format": "SIMPLE_CSV",
  "predicate": {
    "type": "and",
    "predicates": [
      {
        "type": "equals",
        "key": "TAXON_KEY",
        "value": "2927479"
      },
      {
        "type": "equals",
        "key": "YEAR",
        "value": "2020"
      },
      {
        "type": "in",
        "key": "COUNTRY",
        "values": [
          "RU"
        ]
      }
    ]
  }
}

res = requests.post('https://api.gbif.org/v1/occurrence/download/request', json=req_data, auth=('pavel_polonchuk', 'Feature_1'))
instance_code = res.content

print(instance_code)

request_instance_code = instance_code.decode()

print(request_instance_code)

download_base_url = 'https://api.gbif.org/v1/occurrence/download/request/'

req = requests.get(f'{download_base_url}{request_instance_code}.zip', allow_redirects=True)

print(f'{download_base_url}{request_instance_code}.zip')

print(req)

with open('download_res_cuscuta.zip', 'wb') as a_file:
    a_file.write(req.content)
