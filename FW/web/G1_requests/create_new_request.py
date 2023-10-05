from FW.web.any_page import AnyPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class CreateNewRequest(AnyPage):
    def create_new_request_with_sample(self):
        time.sleep(1)
        self.get_driver().find_element(By.XPATH, '//*[@anchor="Requests"]').click()
        time.sleep(2)
        if self.check_new_design():
            self.get_driver().find_element(By.XPATH, '//*[@class="header__button"]').click()
        else:
            self.get_driver().find_element(By.XPATH, '//div[@id="vue_common_placeholder"]//a').click()
            time.sleep(2)
            self.get_driver().find_element(By.XPATH, '//*[@class="header__button"]').click()
        self.get_driver().find_element(By.XPATH, '//*[@id="option-new"]').click()
        self.get_driver().find_element(By.XPATH, '//*[@id="Department_chosen"]').click()
        self.get_driver().find_element(By.XPATH, '//div[@id="Department_chosen"]//input[@class="chosen-search-field"]').send_keys('Отдел тестирования Гандивы', Keys.ENTER)
        self.get_driver().find_element(By.XPATH, '//*[@id="Category_chosen"]').click()
        self.get_driver().find_element(By.XPATH, '//div[@id="Category_chosen"]//input[@class="chosen-search-field"]').send_keys('Программное обеспечение', Keys.ENTER)
        self.get_driver().find_element(By.XPATH, '//*[@id="RequestType_chosen"]').click()
        self.get_driver().find_element(By.XPATH, '//div[@id="RequestType_chosen"]//input[@class="chosen-search-field"]').send_keys('Тестовый', Keys.ENTER)
        self.get_driver().find_element(By.XPATH, '//*[@id="JobType_chosen"]').click()
        self.get_driver().find_element(By.XPATH, '//div[@id="JobType_chosen"]//input[@class="chosen-search-field"]').send_keys('Тестовый', Keys.ENTER)
        frame = self.get_driver().find_element(By.XPATH, '//*[@id="cke_1_contents"]/iframe')
        self.get_driver().switch_to.frame(frame)
        self.get_driver().find_element(By.XPATH, '//*[@class="cke_editable cke_editable_themed cke_contents_ltr"]').send_keys('test')
        self.get_driver().switch_to.default_content()
        self.get_driver().find_element(By.XPATH, '//*[@id="is3"]').click()
        time.sleep(1)

    def check_new_design(self):
        try:
            self.get_driver().find_element(By.XPATH, '//*[@class="header__button"]')
            return True
        except:
            return False