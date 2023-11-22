import json
from json.decoder import JSONDecodeError
import requests
from FW.FW_base import FWBase
import allure


@allure.epic('G1')
@allure.feature('API')
@allure.story('API base методы')
class ApiBase(FWBase):

    @allure.step('GET запрос на получение базового URL')
    def get_base_url(self):
        api_base_url = self.manager.group_data.base_url
        return api_base_url

    @allure.step('GET запрос на получение заголовков')
    def get_header(self):
        headers = {}

        if self.manager.group_data.access_token == '':
            self.manager.api_token.get_token()

        headers['Authorization'] = str(self.manager.group_data.token_type + ' ' + self.manager.group_data.access_token)

        headers['accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        return headers

    @allure.step('Обертка для GET запроса')
    def requests_GET(self, URL, params=None):
        headers = self.get_header()

        response = requests.get(URL, headers=headers, params=params)

        response.encoding = 'utf-8'
        self.request_logs('GET', URL, str(headers), "", str(response.status_code), response.text, params=params)
        assert response.status_code < 500
        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('Обертка для POST запроса')
    def requests_POST(self, URL, body, params=None):
        headers = self.get_header()

        response = requests.post(URL, headers=headers, data=json.dumps(body), params=params)

        response.encoding = 'utf-8'
        self.request_logs('POST', URL, str(headers), str(body), str(response.status_code), response.text, params=params)

        assert response.status_code < 500
        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('Обертка для PUT запроса')
    def requests_PUT(self, URL, body, params=None):
        headers = self.get_header()

        response = requests.put(URL, headers=headers, data=json.dumps(body), params=params)

        response.encoding = 'utf-8'
        self.request_logs('PUT', URL, str(headers), str(body), str(response.status_code), response.text, params=params)
        assert response.status_code < 500
        try:
            return response.json()
        except JSONDecodeError:
            return response

    @allure.step('Обертка для DELETE запроса')
    def requests_DELETE(self, URL, body=None, params=None):
        headers = self.get_header()

        response = requests.delete(URL, headers=headers, data=json.dumps(body), params=params)

        response.encoding = 'utf-8'
        self.request_logs('DELETE', URL, str(headers), "", str(response.status_code), response.text, params=params)
        assert response.status_code < 500
        try:
            return response.json()
        except JSONDecodeError:
            return response
