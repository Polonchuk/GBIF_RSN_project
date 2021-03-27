import requests
import time

# Запрос через API Download сайта GBIF о встречаемости видов указанного рода на территории России с 2016 года по сегодняшний день.
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
        "values": "2927479",
      },
      {
        "type": "greaterThan",
        "key": "YEAR",
        "value": "2015"
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
# Сам запрос
res = requests.post('https://api.gbif.org/v1/occurrence/download/request', json=req_data, auth=('pavel_polonchuk', 'Feature_1'))

# Получение кода ссылки на ответ по запросу
instance_code = res.content
# print(instance_code)

# Превращения кода ссылки из бинарной строки в обычную
request_instance_code = instance_code.decode()
# print(request_instance_code)

# даем сайту GBIF минуту на формирование файла с данными:
time.sleep(60)

# Формирование запроса на получение готовых данных:
download_base_url = 'https://api.gbif.org/v1/occurrence/download/request/'
req = requests.get(f'{download_base_url}{request_instance_code}.zip', allow_redirects=True)

print(f'{download_base_url}{request_instance_code}.zip')
print(req)

with open('download_res_cuscuta_striga_2.zip', 'wb') as a_file:
    a_file.write(req.content)
