from selenium.webdriver.common.by import By
from FW.web.any_page import AnyPage


class EditRequest(AnyPage):
    def get_request_number(self):
        return self.find_element((By.XPATH, '//*[@id="is11"]/div[1]/div[1]/b')).text[2:]

    def approve_request_to_yourself(self):
        self.click_element((By.XPATH, '//*[@data-type="8"]'))

    def cancel_request(self):
        self.click_element((By.XPATH, '//*[@data-type="9"]'))
        frame = self.find_element((By.XPATH, '//*[@id="cke_52_contents"]/iframe'))
        self.get_driver().switch_to.frame(frame)
        self.send_keys((By.XPATH, '//*[@class="cke_editable cke_editable_themed cke_contents_ltr"]'), 'test')
        self.get_driver().switch_to.default_content()
        self.click_element((By.XPATH, '//*[@class="ga_bttn bttn_green"]'))

    def save_request(self):
        self.click_element((By.XPATH, '//*[@id="ga_save_btn"]'))

    def get_request_status(self):
        return self.find_element((By.XPATH, '//*[contains(@class, "ga_status")]')).text

    def get_coordinator_status(self, coordinator):
        element = self.find_element((By.XPATH, f'//*[@id="{coordinator}"]/div/div[3]'))
        result = element.get_attribute('data-tooltip')
        temp = result.find(':')
        return result[:temp]

    def assign_request_to_yourself(self):
        self.click_element((By.XPATH,  '//*[@id="is12"]/div/div/div[@class="ga_change_status"]/button'))

    def transfer_to_examination(self):
        self.click_element((By.XPATH, '//*[@id="to_resolved"]'))

    def give_grade_to_work(self, grade):
        self.click_element((By.XPATH, f'//*[@data-alt="{grade}"]'))
        self.send_keys((By.XPATH, '//*[@id="FeedbackComment"]'), 'test')
