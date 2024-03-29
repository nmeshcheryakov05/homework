import allure
from selenium.webdriver.common.by import By
from FW.web.any_page import AnyPage


class Locator:
    input_login = (By.XPATH, '//input[@id="Input_UserName"]')
    input_password = (By.XPATH, '//input[@id="Input_Password"]')
    local_submit_button = (By.XPATH, '//button[@id="login-submit"]')
    button_remember_me = (By.XPATH, '//input[@id="Input_RememberMe"]')
    error_invalid_login = (By.XPATH, '//div[contains(@class, "validation-summary-errors")]')
    error_empty_password = (By.XPATH, '//span[@id="Input_Password-error"]')
    error_empty_login = (By.XPATH, '//span[@id="Input_UserName-error"]')


@allure.epic('G1')
@allure.feature('WEB')
@allure.story('Методы для работы с авторизацией')
class Login(AnyPage):

    @allure.step('Авторизация по логину и паролю')
    def g1_login_log_pas(self, login=None, password=None):
        if 'Identity' in self.get_current_url():
            if login == None and password == None:
                login = self.manager.group_data.users['user1']['log']
                password = self.manager.group_data.users['user1']['pass']
            self.g1_fill_login(login)
            self.g1_fill_password(password)
            self.g1_click_button_sign_in()
        return self

    @allure.step('Нажатие на поле логина и его ввод')
    def g1_fill_login(self, login):
        self.send_keys(Locator.input_login, login)
        return self

    @allure.step('Нажатие на поле пароля и его ввод')
    def g1_fill_password(self, password):
        self.send_keys(Locator.input_password, password)
        return self

    @allure.step('Нажатие кнопки входа')
    def g1_click_button_sign_in(self):
        self.click_element(Locator.local_submit_button)
        return self

    @allure.step('Выход с текущего пользователя')
    def logout(self):
        self.click_element((By.XPATH, '//*[@data-anchor="profile"]'))
        self.click_element((By.XPATH, '//*[@data-anchor="exit_user"]'))
