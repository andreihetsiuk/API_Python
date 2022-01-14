# import requests
#
# response = requests.get("https://playground.learnqa.ru/api/hello", params={'name': 'Vit'})
# obj = response.json()
# print(obj)

import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'': ''})
obj = response.json()
sec = obj['seconds']
tok = obj['token']
print(obj)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token': tok})
obj = response.json()
print(obj)
assert obj['status'] == 'Job is NOT ready', 'Job is NOT ready is not correct'
time.sleep(sec)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token': tok})
obj = response.text
assert "result" in obj, "field result is not present"
