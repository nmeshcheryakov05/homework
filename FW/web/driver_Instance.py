from selenium import webdriver
import allure


@allure.epic('G1')
@allure.feature('WEB')
@allure.story('Методы для работы с браузером')
class DriverInstance:

    driver = None

    @allure.step('Запуск браузера')
    def start_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver

    @allure.step('Закрытие браузера')
    def stop_driver(self):
        self.driver.quit()
