import requests

def test_auth_user(self):
    data = {
        'email': 'vinkotov@example.com',
        'password': '1234'
    }
    response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)
    print(response1.text)