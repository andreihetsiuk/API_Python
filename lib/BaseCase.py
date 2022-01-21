from requests import Response
import json.decoder

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f'no {cookie_name} in response '
        return response.cookies[cookie_name]

    def get_headers(self, response: Response, headers_name):
        assert headers_name in response.headers, f'no {headers_name} in response '
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, 'response not in JSON format'
        assert name in response_as_dict, f'{name} is not in response_as_dict'

        return response_as_dict[name]

