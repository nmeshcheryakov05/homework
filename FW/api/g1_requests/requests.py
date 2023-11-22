import pytest
import allure
from FW.api.api_base import ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Request запросы')
class Requests(ApiBase):

    @allure.step('PUT запрос на изменение заявки по ID')
    def put_requests_id(self, body, id, params=None):
        return self.requests_PUT(self.get_base_url() + f'/Requests/{id}/Action', body, params)

    @allure.step('GET запрос на получение заявки')
    def get_requests(self, params=None):
        return self.requests_GET(self.get_base_url() + '/Requests', params=params)

    @allure.step('POST запрос на изменение заявки')
    def post_requests(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/Requests', body, params=params)

    @allure.step('GET запрос на получение заявки по ID')
    def get_requests_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/Requests/{id}', params=params)

    @allure.step('DELETE запрос на удаление заявки по ID')
    def delete_requests_id_sub_requests_id(self, id, sub_request_id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/Requests/{id}/SubRequests/{sub_request_id}', params=params)

    @allure.step('GET запрос на получение статуса согласующего')
    def get_approver_status(self, user, response):
        for approver in response['Approvers']:
            if approver['LastName'] == user:
                return approver['Status']
