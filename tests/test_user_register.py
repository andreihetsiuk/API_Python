import requests
from lib.BaseCase import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUserRegister(BaseCase):

    def test_create_new_user(self):

        data = self.prepare_registration_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_status_code(response, 200)

        Assertions.assert_json_has_key(response, "id")

        print(response.content)

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_status_code(response,400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", f"Unexpected content respond {response.content}"
