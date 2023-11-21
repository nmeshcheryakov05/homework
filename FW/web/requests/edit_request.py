from selenium.webdriver.common.by import By
from FW.web.any_page import AnyPage
import time


class EditRequest(AnyPage):

    def page_loading(self):
        self.find_element((By.XPATH, '//*[@id="Description"]'))

    def get_request_number(self):
        return self.find_element((By.XPATH, '//*[@id="is11"]/div[1]/div[1]/b')).text[2:]

    def approve_request_to_yourself(self):
        self.move_to_element((By.XPATH, '//*[@data-type="8"]'))
        self.click_element((By.XPATH, '//*[@data-type="8"]'))
        self.click_element((By.XPATH, '//*[@id="ga_save_btn"]'))

    def cancel_request(self):
        self.move_to_element((By.XPATH, '//*[@data-type="9"]'))
        self.click_element((By.XPATH, '//*[@data-type="9"]'))
        time.sleep(1)
        frame = self.find_element((By.XPATH, '//*[@id="cke_52_contents"]/iframe'))
        self.get_driver().switch_to.frame(frame)
        self.send_keys((By.XPATH, '//*[@class="cke_editable cke_editable_themed cke_contents_ltr"]'), 'test')
        self.get_driver().switch_to.default_content()
        self.click_element((By.XPATH, '//*[@class="ga_bttn bttn_green"]'))

    def save_request(self):
        self.click_element((By.XPATH, '//*[@id="ga_save_btn"]'))
        time.sleep(1)

    def get_request_status(self):
        time.sleep(1)
        return self.find_element((By.XPATH, '//*[contains(@class, "ga_status")]')).text

    def get_coordinator_status(self, coordinator):
        time.sleep(1)
        element = self.find_element((By.XPATH, f'//*[@id="{coordinator}"]/div/div[3]'))
        result = element.get_attribute('data-tooltip')
        temp = result.find(':')
        return result[:temp]

    def assign_request_to_yourself(self):
        self.click_element((By.XPATH, '//*[@class="ga_change_status"]/button'))

    def transfer_to_examination(self):
        self.click_element((By.XPATH, '//*[@id="to_resolved"]'))
        time.sleep(1)

    def give_grade_to_work(self, grade):
        time.sleep(1)
        self.click_element((By.XPATH, f'//*[@data-alt="{grade}"]'))
        self.send_keys((By.XPATH, '//*[@id="FeedbackComment"]'), 'test')

    def presence_of_a_button(self, locator):
        try:
            self.find_element((By.XPATH, f'{locator}'))
            return True
        except:
            return False
