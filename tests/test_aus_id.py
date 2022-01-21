import requests
import pytest
from lib.BaseCase import BaseCase


class TestUserAuth(BaseCase):
    neg_params = [
        'no cookie',
        'no token'
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_headers(response1, "x-csrf-token")
        # assert "auth_sid" in response1.cookies, "auth-sid is no in cookies"
        # assert "x-csrf-token" in response1.headers, "token not in token"
        self.user_id_from_auth_method = self.get_json_value(response1, 'user_id')
        # assert "user_id" in response1.json(), "user_id is absent"

        # self.auth_sid = response1.cookies.get('auth_sid')
        # self.token = response1.headers.get('x-csrf-token')
        # self.user_id_from_auth_method = response1.json()['user_id']

    def test_auth_user(self):

        response2 = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        assert "user_id" in response2.json(), "user_id not in response2"
        user_id_from_check_method = response2.json()['user_id']
        assert user_id_from_check_method == self.user_id_from_auth_method, "not equal"

    @pytest.mark.parametrize("condition", neg_params)
    def test_negative_auth(self, condition):

        if condition == "cookie":
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                headers={"x-csrf-token": self.token}

            )
        else:
            response2 = requests.get(
                'https://playground.learnqa.ru/api/user/auth',
                cookies={"auth_sid": self.auth_sid}

            )
        assert "user_id" in response2.json(), "user_id is absent"
        user_id = response2.json()['user_id']
        assert user_id == 0, 'uer_id not equal 0'
