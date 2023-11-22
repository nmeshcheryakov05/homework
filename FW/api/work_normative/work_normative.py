from FW.api.api_base import ApiBase
import allure


@allure.epic('G1')
@allure.feature('API')
@allure.story('Работа с нормативами')
class WorkNormative(ApiBase):

    @allure.step('GET запрос на получение норматива')
    def work_normative_search(self, params=None):
        return self.requests_GET(self.get_base_url() + '/workNormative/Search', params=params)
