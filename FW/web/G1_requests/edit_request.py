from FW.web.web_base import WebBase
from selenium.webdriver.common.by import By
import time


class EditRequest(WebBase):

    def assign_request_to_yourself(self):
        self.get_driver().find_element(By.XPATH, '//*[@class="ga_bttn_status bttn_e"]').click()
        time.sleep(1)
        self.get_driver().find_element(By.XPATH, '//*[@id="ga_save_btn"]').click()
        time.sleep(3)

    def get_request_number(self):
        return self.get_driver().find_element(By.XPATH, '//*[@id="is11"]/div[1]/div[1]/b').text[2:]

    def get_contractor(self):
        return self.get_driver().find_element(By.XPATH, '//*[@class="ga_user_inline ga_contractor last"]//*[@class="ga_user_name"]').text