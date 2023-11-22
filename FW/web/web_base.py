from selenium.webdriver import ActionChains
import allure
from FW.FW_base import FWBase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.epic('G1')
@allure.feature('WEB')
@allure.story('Методы для работы с драйвером')
class WebBase(FWBase):

    @allure.step('Обертка для работы с драйвером')
    def get_driver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.start_driver()
        return self.manager.driver_instance.driver

    @allure.step('Получение базового URL')
    def get_base_url(self):
        return self.manager.group_data.base_url

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.get_driver().current_url

    @allure.step('Нажатие на элемент страницы')
    def click_element(self, locator):
        web_element = self.find_element(locator)
        web_element.click()

    @allure.step('Отправка клавиш элементу страницы')
    def send_keys(self, locator, text):
        web_element = self.find_element(locator)
        web_element.send_keys(text)

    @allure.step('Поиск элемента страницы')
    def find_element(self, locator, wait=30):
        try:
            web_element = WebDriverWait(self.get_driver(), wait).until(EC.presence_of_element_located(locator))
            return web_element
        except:
            pass

    @allure.step('Поиск элементов страницы')
    def find_elements(self, locator, wait=30):
        try:
            return WebDriverWait(self.get_driver(), wait).until(EC.presence_of_all_elements_located(locator))
        except:
            pass

    @allure.step('Перемещение курсора к элементу страницы')
    def move_to_element(self, locator):
        actions = ActionChains(self.get_driver())
        element = self.find_element(locator)
        actions.move_to_element(element)
        actions.perform()
