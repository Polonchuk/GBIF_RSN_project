import requests

# Запрос через API Download сайта GBIF о встречаемости видов указанного рода на территории России в 2020 году.
# Аттрибуты запроса:
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
        "value": "3171157"
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
# Сам запрос:
res = requests.post('https://api.gbif.org/v1/occurrence/download/request', json=req_data, auth=('pavel_polonchuk', 'Feature_1'))
# Получение кода ссылки на ответ по запросу
instance_code = res.content

print(instance_code)
# Превращения кода ссылки из бинарной строки в обычную
request_instance_code = instance_code.decode()

print(request_instance_code)

download_base_url = 'https://api.gbif.org/v1/occurrence/download/request/'
# Формирование запроса на получение готовых данных (Не срабатывает. 404)
req = requests.get(f'{download_base_url}{request_instance_code}.zip', allow_redirects=True)

print(f'{download_base_url}{request_instance_code}.zip')

print(req)
# Сохранение данных в файл
with open('download_res_striga.zip', 'wb') as a_file:
    a_file.write(req.content)
