from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:

            assert False, f'respose is not in json format, response is {response.text}'

        assert name in response_as_dict, f'Response does not have {name}'
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:

            assert False, f'response is not in json format, response is {response.text}'

        assert name in response_as_dict, f'Response does not have {name}'

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:

            assert False, f'response is not in json format, response is {response.text}'
        for name in names:
            assert name in response_as_dict, f'Response does not have {name}'

    @staticmethod
    def assert_json_has_no_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:

            assert False, f'response is not in json format, response is {response.text}'

        assert name not in response_as_dict, f'Response shouldnt  have {name} but its present'

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code. Expected: {expected_status_code},Actual: {response.status_code}"
