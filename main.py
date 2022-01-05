import requests

#1
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

#2
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params={'method': 'HEAD'})
print(response.text)

#3
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={'method': 'GET'})
print(response.text)


# 4
print('-------GET--------')
for i in ('POST', 'DELETE', 'PUT', 'GET'):
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={'method': i})
    print(response.text)
print('------DELETE---------')
for i in ('POST', 'DELETE', 'PUT', 'GET'):
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': i})
    print(response.text)
print('------PUT---------')
for i in ('POST', 'DELETE', 'PUT', 'GET'):
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': i})
    print(response.text)
print('-------POST--------')
for i in ('POST', 'DELETE', 'PUT', 'GET'):
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': i})
    print(response.text)