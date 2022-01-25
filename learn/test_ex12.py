import requests

def test_ex12():
    response = requests.post("https://playground.learnqa.ru/api/homework_header")
    headers = response.headers
    assert "x-secret-homework-header" in headers, "no secret header in headers"
    assert headers["x-secret-homework-header"] == "Some secret value", "checked value is not equal"

    print(headers)