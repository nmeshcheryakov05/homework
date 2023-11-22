from selenium.webdriver.common.by import By
from FW.web.web_base import WebBase
import allure


@allure.epic('G1')
@allure.feature('WEB')
@allure.story('Методы для любой страницы')
class AnyPage(WebBase):

    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.get_driver().get(self.manager.group_data.base_url_web)

    @allure.step('Открытие страницы заявок')
    def go_to_requests(self):
        self.click_element((By.XPATH, '//*[@data-anchor="Requests"]'))

    @allure.step('Прямой переход на заявку по ее ID')
    def go_to_request_with_request_number(self, request):
        self.get_driver().get(f'https://web-test-compose.gandiva.ru/Request/Edit/{request}')
