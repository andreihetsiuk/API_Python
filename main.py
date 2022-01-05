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

for i in ('POST', 'DELETE', 'PUT', 'GET'):
    for j in ('post', 'delete', 'put', 'get'):
        response = requests.request(j, "https://playground.learnqa.ru/ajax/api/compare_query_type",
                                    params={'method': i})
        print(response.text)
    print("-----", i, "/", j, "------")

