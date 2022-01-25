import requests

def test_ex11():
    response = requests.post("https://playground.learnqa.ru/api/homework_cookie")
    cookie = dict(response.cookies)

    assert "HomeWork" in cookie
    assert cookie["HomeWork"] == "hw_value"
    print(dict(cookie))





