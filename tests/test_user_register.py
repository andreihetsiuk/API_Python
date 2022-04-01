import requests
from lib.BaseCase import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': 'user',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"status code isn't 400"
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", f"Unexpected content respond {response.content}"
