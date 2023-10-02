from FW.web.any_page import AnyPage
from selenium.webdriver.common.by import By
import time


class Main(AnyPage):
    def open_main_page(self):
        self.get_driver().get('https://web-test-compose.gandiva.ru/Identity/Account/Login?ReturnUrl=%2F')

    def login_test_user1(self):
        self.get_driver().find_element(By.XPATH, '//*[@id="Input_UserName"]').send_keys('gandiva_test_user1@mail.ru')
        self.get_driver().find_element(By.XPATH, '//*[@id="Input_Password"]').send_keys('Qwerty1!')
        self.get_driver().find_element(By.XPATH, '//*[@id="login-submit"]').click()
        time.sleep(2)

    def login_test_boss1(self):
        self.get_driver().find_element(By.XPATH, '//*[@id="Input_UserName"]').send_keys('gandiva_test_boss_1@mail.ru')
        self.get_driver().find_element(By.XPATH, '//*[@id="Input_Password"]').send_keys('Qwerty1!')
        self.get_driver().find_element(By.XPATH, '//*[@id="login-submit"]').click()
        time.sleep(2)

    def logout(self):
        self.get_driver().find_element(By.XPATH, '//*[@anchor="profile"]').click()
        self.get_driver().find_element(By.XPATH, '//*[@anchor="exit_user"]').click()