from FW.FW_base import FWBase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WebBase(FWBase):

    def get_driver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.start_driver()
        return self.manager.driver_instance.driver

    def get_base_url(self):
        return self.manager.group_data.base_url

    def get_current_url(self):
        return self.get_driver().current_url

    def click_element(self, locator):
        web_element = self.find_element(locator)
        web_element.click()

    def send_keys(self, locator, text):
        web_element = self.find_element(locator)
        web_element.send_keys(text)

    def find_element(self, locator, wait=30):
        try:
            web_element = WebDriverWait(self.get_driver(), wait).until(EC.presence_of_element_located(locator))
            return web_element
        except:
            pass

    def find_elements(self, locator, wait=30):
        try:
            return WebDriverWait(self.get_driver(), wait).until(EC.presence_of_all_elements_located(locator))
        except:
            pass
