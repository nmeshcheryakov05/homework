from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from FW.web.any_page import AnyPage


class CreateRequest(AnyPage):
    def check_new_design(self):
        try:
            self.find_element((By.XPATH, '//*[@id="vue_common_placeholder"]'))
            return True
        except:
            return False

    def create_new_default_request(self):
        if self.check_new_design():
            self.click_element((By.XPATH, '//*[@id="vue_common_placeholder"]'))
        self.click_element((By.XPATH, '//div[@class="header__button"]'))
        self.click_element((By.XPATH, '//*[@id="option-new"]'))

    def gandiva_test_department_choose(self):
        self.click_element((By.XPATH, '//*[@id="Department_chosen"]'))
        self.send_keys((By.XPATH, '//div[@id="Department_chosen"]//input[@class="chosen-search-field"]'),
                       ('Отдел тестирования Гандивы', Keys.ENTER))

    def software_category_choose(self):
        self.click_element((By.XPATH, '//*[@id="Category_chosen"]'))
        self.send_keys((By.XPATH, '//div[@id="Category_chosen"]//input[@class="chosen-search-field"]'),
                       ('Программное обеспечение', Keys.ENTER))

    def test_type_choose(self):
        self.click_element((By.XPATH, '//*[@id="RequestType_chosen"]'))
        self.send_keys((By.XPATH, '//div[@id="RequestType_chosen"]//input[@class="chosen-search-field"]'),
                           ('Тестовый', Keys.ENTER))

    def test_job_type_choose(self):
        self.click_element((By.XPATH, '//*[@id="JobType_chosen"]'))
        self.send_keys((By.XPATH, '//div[@id="JobType_chosen"]//input[@class="chosen-search-field"]'),
                       ('Тестовый', Keys.ENTER))

    def test_description(self):
        frame = self.find_element((By.XPATH, '//*[@id="cke_1_contents"]/iframe'))
        self.get_driver().switch_to.frame(frame)
        self.send_keys((By.XPATH, '//*[@class="cke_editable cke_editable_themed cke_contents_ltr"]'), 'test')
        self.get_driver().switch_to.default_content()

    def add_coordinator(self, user, result):
        self.click_element((By.XPATH, '//*[@data-handler="request_agreement_build"]'))
        self.click_element((By.XPATH, '//div[@id="get_user_request_chosen"]'))
        self.send_keys((By.XPATH, '//div[@id="get_user_request_chosen"]//input[@class="chosen-search-field"]'), user)
        self.click_element((By.XPATH, f'//*[@id="get_user_request_chosen"]/div/ul/li[{result}]'))
