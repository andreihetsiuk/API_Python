import requests
class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)
        assert "auth_sid" in response1.cookies, "auth-sid is no in cookies"
        assert "x-csrf-token" in response1.headers, "token not in token"
        assert "user_id" in response1.json(), "user_id is absent"

        auth_sid = response1.cookies.get('auth_sid')
        token = response1.headers.get('x-csrf-token')
        user_id_from_auth_method = response1.json()['user_id']

        response2 = requests.get(
            'https://playground.learnqa.ru/api/user/auth',
            headers={"x-csrf-token": token},
            cookies={"auth_id": auth_sid}
        )
        print(token)
        assert "user_id" in response2.json(), "user_id not in response2"
        user_id_from_check_method = response2.json()['user_id']
        assert user_id_from_check_method == user_id_from_auth_method, "not equal"
