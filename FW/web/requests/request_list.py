import time
from selenium.webdriver.common.by import By
from FW.web.any_page import AnyPage

class RequestList(AnyPage):

    def page_loading(self):
        time.sleep(2)

    def check_new_design(self):
        try:
            self.find_element((By.XPATH, '//*[@id="vue_common_placeholder"]'))
            return True
        except:
            return False

    def create_new_default_request(self):
        self.page_loading()
        if self.check_new_design():
            self.click_element((By.XPATH, '//*[@id="vue_common_placeholder"]'))
        self.page_loading()
        self.click_element((By.XPATH, '//div[@class="header__button"]'))
        self.click_element((By.XPATH, '//*[@id="option-new"]'))
