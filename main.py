import requests

# payload = {"name": "user"}

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print(response.history)
print(response.history[2].url)
