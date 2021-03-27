import requests
import time

# Запрос через API Download сайта GBIF о встречаемости указанных видов на территории России с 2016 года по сегодняшний день.
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
        "type": "in",
        "key": "TAXON_KEY",
        "values": [
          "3142214",
          "8002952",
          "3110686",
          "3110588",
          "5289731",
          "2930922",
          "2931237",
          "3678256",
          "3610757",
          "2927493",
          "2927518",
          "2927548",
          "2927520",
          "7428299",
          "7361176",
          "5391845",
          "3066993",
          "3119239",
          "3119230",
          "2928538",
          "2928584",
          "5402631",
          "2932011",
          "2929892"
          ]
      },
      {
        "type": "greaterThan",
        "key": "YEAR",
        "value": "2015"
      },
      {
        "type": "equals",
        "key": "COUNTRY",
        "value": "RU"
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
time.sleep(120)

# Формирование запроса на получение готовых данных:
download_base_url = 'https://api.gbif.org/v1/occurrence/download/request/'
req = requests.get(f'{download_base_url}{request_instance_code}.zip', allow_redirects=True)

print(f'{download_base_url}{request_instance_code}.zip')
print(req)

with open('download_all_species.zip', 'wb') as a_file:
    a_file.write(req.content)
