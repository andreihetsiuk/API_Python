import requests
import json
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'': ''})
obj = response.text
obj = json.loads(obj)
sec = obj['seconds']
tok = obj['token']
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token': tok})
obj = response.text
obj = json.loads(obj)
assert (obj['status']) == 'Job is NOT ready'
time.sleep(sec)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={'token': tok})
obj = response.text
obj = json.loads(obj)
assert (obj['status']) == 'Job is ready'
if 'result' in obj:
    pass
else:
    print(f'result is absent')



